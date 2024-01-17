from django.db import models
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_consent.validators import eligible_if_yes
from edc_consent.managers import ConsentManager
from edc_search.model_mixins import SearchSlugManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import ConsentModelMixin
from edc_search.model_mixins import SearchSlugModelMixin
from django_crypto_fields.fields import EncryptedCharField
from django.core.validators import RegexValidator
from edc_consent.field_mixins import IdentityFieldsMixin, ReviewFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin, VulnerabilityFieldsMixin
from edc_base.model_validators import datetime_not_future, date_not_future
from edc_protocol.validators import datetime_not_before_study_start
from ...choices import IDENTITY_TYPE, GENDER_OTHER
from edc_base.model_fields import OtherCharField
from edc_base.sites import CurrentSiteManager
from edc_base.model_managers import HistoricalRecords
from edc_base.utils import get_utcnow
from .eligibility import FacetConsentEligibility
from django.apps import apps as django_apps


class FacetConsent(ConsentModelMixin, SiteModelMixin,
                   NonUniqueSubjectIdentifierFieldMixin,
                   IdentityFieldsMixin, SearchSlugModelMixin,
                   ReviewFieldsMixin, PersonalFieldsMixin,
                   VulnerabilityFieldsMixin, BaseUuidModel):
    subject_screening_model = 'flourish.facetsubjectscreening'

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))],
        help_text=('Ensure initials consist of letters '
                   'only in upper case, no spaces.'),
        null=True, blank=False)

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        help_text='Date and time of consent.',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future])

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=30,
        choices=IDENTITY_TYPE)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_OTHER,
        max_length=5,
        null=True,
        blank=False)

    consent_to_participate = models.CharField(
        verbose_name='Do you consent to participate in the facet study?',
        choices=YES_NO,
        max_length=3,
        validators=[eligible_if_yes, ],
        help_text='If no, participant is not eligible.')

    child_consent = models.CharField(
        max_length=3,
        verbose_name='Are you willing to consent for your child’s participation in FACET?',
        choices=YES_NO_NA,
        help_text='If ‘No’ ineligible for study participation')

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    gender_other = OtherCharField()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def natural_key(self):
        return self.subject_identifier, self.version

    def save(self, *args, **kwargs):
        self.version = '1'
        super().save(*args, **kwargs)

    @property
    def consent_version(self):
        return self.version

    @property
    def hiv_status(self):
        if self.subject_identifier:
            helper = MaternalStatusHelper(
                subject_identifier=self.subject_identifier)
            return helper.hiv_status

    @property
    def consent_child_age(self):
        return child_age_in_months(self.consent_datetime.date(),
                                   self.subject_identifier)

    @property
    def current_child_age(self):
        return child_age_in_months(get_utcnow().date(),
                                   self.subject_identifier)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('subject_identifier')
        return fields

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Facet Consent'
        verbose_name_plural = 'Facet Consent'
        unique_together = (('subject_identifier',),)
        consent_group = django_apps.get_app_config(
            'edc_consent').default_consent_group

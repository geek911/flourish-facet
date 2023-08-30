from django.db import models
from ..mother import FacetConsent
from django_crypto_fields.fields import FirstnameField, LastnameField
from django_crypto_fields.fields import IdentityField
from edc_constants.choices import GENDER, YES_NO
from ...choices import CHILD_IDENTITY_TYPE, CHILD_CONSENT_VERSION
from edc_base.model_validators import datetime_not_future, date_not_future
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_protocol.validators import datetime_not_before_study_start
from django.core.validators import MaxValueValidator, MinValueValidator
from edc_consent.field_mixins import VerificationFieldsMixin
from edc_base.model_mixins import BaseUuidModel


class MotherChildConsent(SiteModelMixin, NonUniqueSubjectIdentifierFieldMixin,
                         IdentityFieldsMixin, PersonalFieldsMixin,
                         VerificationFieldsMixin, BaseUuidModel):

    facet_consent = models.ForeignKey(
        FacetConsent,
        on_delete=models.PROTECT
    )

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    first_name = FirstnameField(
        null=True, blank=True)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=True)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,
        blank=True)

    identity = IdentityField(
        verbose_name='Identity number',
        null=True,
        blank=True)

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=CHILD_IDENTITY_TYPE,
        null=True,
        blank=True)

    confirm_identity = IdentityField(
        help_text='Retype the identity number',
        null=True,
        blank=True)

    child_dob = models.DateField(
        verbose_name="Date of birth",
        validators=[date_not_future, ],
        null=True,
        blank=True)

    child_test = models.CharField(
        verbose_name='Will you allow for HIV testing and counselling of '
                     'your Child',
        max_length=5,
        choices=YES_NO,
        help_text='If no, participant is not eligible.')

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future])

    caregiver_visit_count = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        blank=True,
        null=True)

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    ineligibility = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Mother Consent On Behalf Of Child'
        verbose_name_plural = 'Mother Consent On Behalf Of Child'

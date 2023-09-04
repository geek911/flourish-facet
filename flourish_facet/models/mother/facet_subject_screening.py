from django.db import models
from edc_constants.choices import YES_NO, YES
from edc_base.utils import get_utcnow
from edc_protocol.validators import datetime_not_before_study_start
from edc_base.model_validators import datetime_not_future
from edc_base.model_fields import OtherCharField
from ...choices import REASONS_UNWILLING_FACET
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel


class FacetSubjectScreening(NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin,
                            BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Report Time and Date',
        default=get_utcnow,
        validators=[datetime_not_future, datetime_not_before_study_start],)

    facet_participation = models.CharField(
        verbose_name='Participant willing to do an Informed consent for the Facet Study',
        choices=YES_NO,
        max_length=10,
        help_text='Ineligible for Facet Study if No'
    )

    hiv_testing = models.CharField(
        verbose_name='Participant willing to go under HIV testing?',
        choices=YES_NO,
        max_length=10,
        null=True,
        blank=True,
        help_text='Ineligible for Facet Study if No'
    )

    reasons_unwilling_part = models.CharField(
        verbose_name='Reasons unable to obtain an informed consent for Facet study',
        choices=REASONS_UNWILLING_FACET,
        max_length=50,
        blank=True,
        null=True
    )
    reasons_unwilling_part_other = OtherCharField()

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    def save(self, *args, **kwargs):
        self.is_eligible = self.facet_participation == YES\
            and self.hiv_testing == YES
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Facet Study Screening'
        verbose_name_plural = 'Facet Study Screening'
        unique_together = (('subject_identifier',),)


from django.db import models
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from ...choices import COMPLETE_UNVERIFIED, QUALITATIVE_TYPE
from edc_constants.choices import YES_NO


class QualitativeInterviewScheduling(NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin, BaseUuidModel):

    qualitative_type = models.CharField(
        verbose_name='You indicated this participant is participating in a qualitative interview. Is the participant participating in a focus group discussion or an in-depth interview?',
        choices=QUALITATIVE_TYPE,
        max_length=25,
    )

    google_sheet_calendar = models.CharField(
        verbose_name=(
            'Has this participant been added to the Google Sheets calendar?'),
        choices=YES_NO,
        max_length=5,
        help_text=('Please ensure the participant is available and able to attend the interview they are scheduled for.'
                   ' Add in the scheduled date in the Google Sheet calendar'),
    )

    facet_consent_form = models.CharField(
        verbose_name=(
            'Confirm this consent form has been added scanned and saved in the FACET Dropbox'),
        choices=YES_NO,
        max_length=5,
    )
    complete = models.CharField(
        verbose_name='Complete?',
        choices=COMPLETE_UNVERIFIED,
        max_length=15
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Qualitative Interview Scheduling'
        verbose_name_plural = 'Qualitative Interview Scheduling'

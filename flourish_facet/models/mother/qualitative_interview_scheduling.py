from django.db import models
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from ...choices import COMPLETE_UNVERIFIED, QUALITATIVE_TYPE
from edc_constants.choices import YES_NO
from edc_base.utils import get_utcnow
from edc_base.model_validators import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start
from django.core.validators import FileExtensionValidator


class QualitativeInterviewScheduling(NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin,
                                     BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

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

    facet_consent_form = models.FileField(
        upload_to='facet_interview/consents/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])

    complete = models.CharField(
        verbose_name='Complete?',
        choices=COMPLETE_UNVERIFIED,
        max_length=15
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Qualitative Interview Scheduling'
        verbose_name_plural = 'Qualitative Interview Scheduling'

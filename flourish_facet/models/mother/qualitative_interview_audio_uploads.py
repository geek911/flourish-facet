from django.db import models
from edc_base.model_validators import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start
from edc_base.utils import get_utcnow
from flourish_facet.choices import COMPLETE_UNVERIFIED, LOCATION_INTERVIEW, LANGUAGES_BOTH
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO_NA
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import FileExtensionValidator
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin


class QualitativeInterviewAudioUploads(NonUniqueSubjectIdentifierFieldMixin,
                                       SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Interview Date and Time',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text='Date and time of this interview')

    location = models.CharField(
        verbose_name='Location of interview',
        choices=LOCATION_INTERVIEW,
        max_length=25,
    )

    location_other = OtherCharField()

    interview_duration = models.PositiveIntegerField(
        verbose_name="Duration of interview",
        validators=[MinValueValidator(10), MaxValueValidator(1440)],
        help_text='Minutes')

    interview_language = models.CharField(
        verbose_name='In what language was the interview performed?',
        choices=LANGUAGES_BOTH,
        max_length=15,
    )
    audio_file = models.FileField(
        upload_to='facet_interview/audios',
        validators=[FileExtensionValidator(['mp3'])],
        max_length=254,
        null=True)

    notes = models.FileField(
        upload_to='facet_interview/notes/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Qualitative Interview Audio Uploads'
        verbose_name_plural = 'Qualitative Interview Audio Uploads'

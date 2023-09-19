from django.db import models
from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from ...choices import COMPLETE_UNVERIFIED, TRANSCRIPTION_HOURS, FACET_STAFF
from edc_constants.choices import YES_NO_NA, YES_NO
from edc_base.model_validators import date_not_future
from edc_protocol.validators import date_not_before_study_start
from edc_base.utils import get_utcnow


class QualitativeInterviewTranscriptionAndTranslation(NonUniqueSubjectIdentifierFieldMixin,
                                                      SiteModelMixin, BaseUuidModel):

    transcription_date = models.DateField(
        verbose_name='Date transcription completed',
        validators=[date_not_before_study_start, date_not_future],
    )
    transcription_upload = models.CharField(
        verbose_name=(
            'Was the transcription file of the interview uploaded to Dropbox?'),
        choices=YES_NO,
        max_length=5,
    )
    facet_member_transcription = models.CharField(
        verbose_name='Which FACET staff member completed the transcription?',
        choices=FACET_STAFF,
        max_length=10,
    )
    transcription_duration = models.CharField(
        verbose_name=(
            'Approximately how long did it take to complete the transcription?'),
        choices=TRANSCRIPTION_HOURS,
        max_length=10,
    )
    translation_date = models.DateField(
        verbose_name='Date translation completed',
        validators=[date_not_before_study_start, date_not_future],
    )
    translation_upload = models.CharField(
        verbose_name=(
            'Was the translation file uploaded to Dropbox? '),
        choices=YES_NO_NA,
        max_length=5,
    )
    facet_member_translation = models.CharField(
        verbose_name='Which FACET staff member completed the translation?',
        choices=FACET_STAFF,
        max_length=10,
    )

    complete = models.CharField(
        verbose_name='Complete?',
        choices=COMPLETE_UNVERIFIED,
        max_length=15
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Qualitative Interview Transcription And Translation'
        verbose_name_plural = 'Qualitative Interview Transcription And Translation'

from django.db import models
from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future, date_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start, date_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_base.model_fields.custom_fields import OtherCharField
from ...action_items import FACET_CHILD_OFFSTUDY_ACTION
from flourish_prn.choices import CHILD_OFF_STUDY_REASON
from flourish_prn.models.offstudy_model_mixin import OffStudyModelMixin


class FacetChildOffSchedule(OffStudyModelMixin,
                            OffScheduleModelMixin,
                            ActionModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'FC'

    action_name = FACET_CHILD_OFFSTUDY_ACTION

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    """ A model completed by the user when the child is taken off study. """

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    reason = models.CharField(
        verbose_name=('Please code the primary reason the participant is'
                      ' being taken off the study'),
        max_length=115,
        choices=CHILD_OFF_STUDY_REASON)

    offstudy_date = models.DateField(default=get_utcnow)

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,)

    schedule_name = models.CharField(max_length=50)

    history = HistoricalRecords()

    consent_version = models.CharField(default='1', max_length=3)

    class Meta:
        verbose_name = 'Facet Child Off-Study'
        verbose_name_plural = 'Facet Child Off-Study'

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
from ..model_mixins import FacetOffScheduleMixin
from ...action_items import FACET_CHILD_OFFSTUDY_ACTION


class FacetChildOffSchedule(FacetOffScheduleMixin):

    tracking_identifier_prefix = 'FC'

    action_name = FACET_CHILD_OFFSTUDY_ACTION

    class Meta:
        verbose_name = 'Facet Child Off-Study'
        verbose_name_plural = 'Facet Child Off-Study'

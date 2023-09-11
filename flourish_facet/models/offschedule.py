from django import forms
from django.apps import apps as django_apps
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_identifier.managers import SubjectIdentifierManager

from edc_visit_schedule.model_mixins import OffScheduleModelMixin


class FacetMotherOffSchedule(OffScheduleModelMixin, BaseUuidModel):
    class Meta:
        app_label = 'flourish_facet'


class FacetChildOffSchedule(OffScheduleModelMixin, BaseUuidModel):
    class Meta:
        app_label = 'flourish_facet'

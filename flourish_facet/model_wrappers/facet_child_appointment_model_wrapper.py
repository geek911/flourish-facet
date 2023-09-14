from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_subject_dashboard import AppointmentModelWrapper as BaseAppointmentModelWrapper

from .facet_child_visit_model_wrapper import ChildVisitModelWrapper


class ChildAppointmentModelWrapper(BaseAppointmentModelWrapper):
    model = 'flourish_facet.appointment'
    dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_child_dashboard_url')
    visit_model_wrapper_cls = ChildVisitModelWrapper
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_child_dashboard_url')
    dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_child_dashboard_url')

    @property
    def wrapped_visit(self):
        """Returns a wrapped persistent or non-persistent visit instance.
        """
        try:
            model_obj = self.object.facetvisit
        except ObjectDoesNotExist:
            visit_model = django_apps.get_model(
                self.visit_model_wrapper_cls.model)
            model_obj = visit_model(
                appointment=self.object,
                subject_identifier=self.subject_identifier,
                reason=self.object.appt_reason)
        return self.visit_model_wrapper_cls(model_obj=model_obj)

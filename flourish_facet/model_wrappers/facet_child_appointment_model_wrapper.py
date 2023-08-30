from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_subject_dashboard import AppointmentModelWrapper as BaseAppointmentModelWrapper

from .facet_mother_visit_model_wrapper import MotherVisitModelWrapper


class ChildAppointmentModelWrapper(BaseAppointmentModelWrapper):
    model = 'flourish_facet.appointment'
    dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_mother_dashboard_url')
    visit_model_wrapper_cls = MotherVisitModelWrapper
    next_url_name = settings.DASHBOARD_URL_NAMES.get('facet_mother_dashboard_url')

    @property
    def wrapped_visit(self):
        """Returns a wrapped persistent or non-persistent visit instance.
        """
        try:
            model_obj = self.object.facevisit
        except ObjectDoesNotExist:
            visit_model = django_apps.get_model(
                self.visit_model_wrapper_cls.model)
            model_obj = visit_model(
                appointment=self.object,
                subject_identifier=self.subject_identifier,
                reason=self.object.appt_reason)
        return self.visit_model_wrapper_cls(model_obj=model_obj)

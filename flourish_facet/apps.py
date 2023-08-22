from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'flourish_facet'
    verbose_name = 'Flourish Facet'
    admin_site_name = 'flourish_facet_admin'


if settings.APP_NAME == 'flourish_facet':
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='flourish_facet.maternalvisit',
                appt_type='clinic'),
            AppointmentConfig(
                model='flourish_facet.childappointment',
                related_visit_model='flourish_facet.facetchildvisit',
                appt_type='clinic'),
        ]

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'flourish_facet': (
                'maternal_visit', 'flourish_facet.maternalvisit'),
            'flourish_facet': (
                'facet_child_visit', 'flourish_facet.facetchildvisit'),
        }

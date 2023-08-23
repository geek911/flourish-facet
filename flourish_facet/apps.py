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
    from edc_base.apps import AppConfig as BaseEdcBaseAppConfig

    class EdcBaseAppConfig(BaseEdcBaseAppConfig):
        project_name = 'Flourish Facet'
        institution = 'Botswana-Harvard AIDS Institute'

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        configurations = [
            AppointmentConfig(
                model='flourish_facet.appointment',
                related_visit_model='flourish_facet.facetvisit',
                appt_type='clinic'),
        ]

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'flourish_facet': (
                'facet_visit', 'flourish_facet.facetvisit'),
        }

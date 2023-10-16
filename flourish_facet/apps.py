from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_odk.apps import AppConfig as BaseEdcOdkAppConfig


class AppConfig(DjangoAppConfig):
    name = 'flourish_facet'
    verbose_name = 'Flourish Facet'
    admin_site_name = 'flourish_facet_admin'


class EdcOdkAppConfig(BaseEdcOdkAppConfig):
    adult_child_study = False
    adult_consent_model = 'flourish_caregiver.subjectconsent'
    child_assent_model = 'flourish_child.childassent'
    clinician_notes_form_ids = {
        'flourish_child': 'child_cliniciannotes_v1.0',
        'flourish_caregiver': 'caregiver_cliniciannotes_v1.0'}

    clinician_notes_models = {
        'flourish_child': 'childcliniciannotes',
        'flourish_caregiver': 'cliniciannotes'}


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
        'flourish_caregiver': (
            'maternal_visit', 'flourish_caregiver.maternalvisit'),
        'flourish_child': (
            'child_visit', 'flourish_child.childvisit'),
        'pre_flourish': (
            'maternal_visit', 'pre_flourish.preflourishcaregivervisit'),
    }

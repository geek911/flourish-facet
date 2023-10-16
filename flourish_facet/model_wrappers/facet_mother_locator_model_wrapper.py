from django.apps import apps as django_apps
from django.conf import settings
from django.db.models import Q
from edc_constants.constants import YES
from edc_model_wrapper import ModelWrapper


class LocatorModelWrapper(ModelWrapper):
    model = 'flourish_caregiver.caregiverlocator'
    querystring_attrs = ['screening_identifier', 'subject_identifier',
                         'study_maternal_identifier', 'first_name', 'last_name']
    next_url_attrs = ['subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_mother_dashboard_url')


from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper

class FacetConsentModelWrapper(ModelWrapper):
    model = 'flourish_facet.facetconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('flourish_facet_consent_listboard_url')
    next_url_attrs = []
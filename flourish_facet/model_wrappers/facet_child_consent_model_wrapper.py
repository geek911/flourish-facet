
from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper


class FacetChildConsentModelWrapper(ModelWrapper):
    model = 'flourish_facet.motherchildconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_child_listboard_url')
    next_url_attrs = []

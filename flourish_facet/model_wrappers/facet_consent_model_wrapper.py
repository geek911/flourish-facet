
from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper

class FacetConsentModelWrapper(ModelWrapper):
    model = 'flourish_facet.facetconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('facet_flourish_consent_listboard_url')
    next_url_attrs = ['subject_identifier',]
    querystring_attrs = ['subject_identifier','first_name',
                         'last_name','initials','language',
                         'is_literate','witness_name','gender',
                         'gender_other','dob','is_dob_estimated',
                         'identity','identity_type','confirm_identity',
                         'consent_to_participate','child_consent',]
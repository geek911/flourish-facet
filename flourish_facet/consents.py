from django.apps import apps as django_apps
from edc_constants.constants import MALE, FEMALE
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from flourish_caregiver.consent_object_validator import ConsentObjectValidator

edc_protocol = django_apps.get_app_config('edc_protocol')


facet_consent_v1 = Consent(
    'flourish_facet.facetconsent',
    version='1',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=18,
    age_is_adult=18,
    age_max=110,
    gender=[FEMALE,])



facet_child_consent_v1 = Consent(
    'flourish_facet.motherchildconsent',
    version='1',
    gender=[FEMALE,MALE],
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,)

site_consents.validator_cls = ConsentObjectValidator

site_consents.register(facet_consent_v1)
site_consents.register(facet_child_consent_v1)
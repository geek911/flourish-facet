from django.conf import settings
from edc_subject_dashboard import SubjectVisitModelWrapper as BaseSubjectVisitModelWrapper


class FacetScreeningModelWrapper(BaseSubjectVisitModelWrapper):

    model = 'flourish_facet.facetsubjectscreening'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_flourish_consent_listboard_url')
    next_url_attrs = ['subject_identifier']

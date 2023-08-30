from django.conf import settings
from edc_subject_dashboard import SubjectVisitModelWrapper as BaseSubjectVisitModelWrapper


class ChildVisitModelWrapper(BaseSubjectVisitModelWrapper):

    model = 'flourish_facet.facetvisit'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('facet_mother_dashboard_url')
    next_url_attrs = ['subject_identifier', 'appointment']

from django.conf import settings
from edc_model_wrapper import ModelWrapper


class QualitativeInterviewSchedulingModelWrapper(ModelWrapper):

    model = 'flourish_facet.qualitativeinterviewscheduling'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_mother_dashboard_url')
    next_url_attrs = ['subject_identifier']

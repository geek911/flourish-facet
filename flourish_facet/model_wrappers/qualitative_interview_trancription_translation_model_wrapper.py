from django.conf import settings
from edc_model_wrapper import ModelWrapper


class QualitativeInterviewTranscriptionAndTranslationModelWrapper(ModelWrapper):

    model = 'flourish_facet.qualitativeinterviewtranscriptionandtranslation'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_mother_dashboard_url')
    next_url_attrs = ['subject_identifier']

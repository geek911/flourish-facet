from django.conf import settings
from edc_model_wrapper import ModelWrapper


class FocusGroupInterviewTranscriptionAndTranslationModelWrapper(ModelWrapper):

    model = 'flourish_facet.focusgroupinterviewtranscriptionandtranslation'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'group_interview_listboard_url')
    next_url_attrs = ['group_identifier']


from django.conf import settings
from edc_model_wrapper import ModelWrapper
from flourish_facet.model_wrappers.focus_group_interview_audio_upload_model_wrapper_mixin import (
    FocusGroupInterviewAudioUploadModelWrapperMixin)
from .focus_group_interview_trancription_translation_model_wrapper_mixin import (
    FocusGroupInterviewTranscriptionAndTranslationModelWrapperMixin)


class FocusGroupInterviewAudioUploadModelWrapper(FocusGroupInterviewAudioUploadModelWrapperMixin,
                                                 FocusGroupInterviewTranscriptionAndTranslationModelWrapperMixin,
                                                 ModelWrapper):

    model = 'flourish_facet.focusgroupinterviewaudiouploads'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'group_interview_listboard_url')
    next_url_attrs = ['group_identifier']

    @property
    def focus_group_interview_audio_upload_model_wrapper_cls(self):

        return self

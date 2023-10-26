
from django.conf import settings
from edc_model_wrapper import ModelWrapper
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps as django_apps
from .focus_group_interview_trancription_translation_model_wrapper_mixin import FocusGroupInterviewTranscriptionAndTranslationModelWrapperMixin


class FocusGroupInterviewAudioUploadModelWrapper(FocusGroupInterviewTranscriptionAndTranslationModelWrapperMixin, ModelWrapper):

    model = 'flourish_facet.focusgroupinterviewaudiouploads'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'group_interview_listboard_url')
    next_url_attrs = ['group_identifier']

    @property
    def focus_group_interview_audio_upload(self):
        """Returns a wrapped unsaved qualitative interview audio upload.
        """
        model_obj = self.focus_group_interview_audio_upload_model_obj or \
            self.focus_group_interview_audio_upload_cls(
                **self.focus_group_interview_audio_upload_options)
        return self(model_obj=model_obj)

    @property
    def focus_group_interview_audio_upload_model_obj(self):
        """Returns a qualitative interview audio upload instance or None.
        """
        try:
            return self.focus_group_interview_audio_upload_cls.objects.get(
                **self.focus_group_interview_audio_upload_options)
        except ObjectDoesNotExist:
            return None

    @property
    def focus_group_interview_audio_upload(self):
        """Returns a wrapped unsaved qualitative interview audio upload.
        """
        model_obj = self.focus_group_interview_audio_upload_model_obj or \
            self.focus_group_interview_audio_upload_cls(
                **self.create_focus_group_interview_audio_upload_options)
        return self(model_obj=model_obj)

    @property
    def focus_group_interview_audio_upload_cls(self):
        return django_apps.get_model('flourish_facet.focusgroupinterviewaudiouploads')

    @property
    def create_focus_group_interview_audio_upload_options(self):
        """Returns a dictionary of options to create a new
        unpersisted qualitative interview audio upload model instance.
        """
        options = dict(
            group_identifier=self.object.group_identifier)
        return options

    @property
    def focus_group_interview_audio_upload_options(self):
        """Returns a dictionary of options to get an existing
        qualitative interview audio upload model instance.
        """
        options = dict(
            group_identifier=self.object.group_identifier)
        return options

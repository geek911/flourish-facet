from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .focus_group_interview_trancription_translation_model_wrapper import FocusGroupInterviewTranscriptionAndTranslationModelWrapper


class FocusGroupInterviewTranscriptionAndTranslationModelWrapperMixin:

    focus_group_interview_transcription_translation_model_wrapper_cls = FocusGroupInterviewTranscriptionAndTranslationModelWrapper

    @property
    def focus_group_interview_transcription_translation_model_obj(self):
        """Returns a focus group interview transcription and translation instance or None.
        """
        try:
            return self.focus_group_interview_transcription_translation_cls.objects.get(
                **self.focus_group_interview_transcription_translation_options)
        except ObjectDoesNotExist:
            return None

    @property
    def focus_group_interview_transcription_translation(self):
        """Returns a wrapped unsaved focus group interview transcription and translation.
        """
        model_obj = self.focus_group_interview_transcription_translation_model_obj or \
            self.focus_group_interview_transcription_translation_cls(
                **self.create_focus_group_interview_transcription_translation_options)
        return self.focus_group_interview_transcription_translation_model_wrapper_cls(model_obj=model_obj)

    @property
    def focus_group_interview_transcription_translation_cls(self):
        return django_apps.get_model('flourish_facet.focusgroupinterviewtranscriptionandtranslation')

    @property
    def create_focus_group_interview_transcription_translation_options(self):
        """Returns a dictionary of options to create a new
        unpersisted focus group interview transcription and translation model instance.
        """
        options = dict(
            group_identifier=self.object.group_identifier)
        return options

    @property
    def focus_group_interview_transcription_translation_options(self):
        """Returns a dictionary of options to get an existing
        focus group interview transcription and translation model instance.
        """
        options = dict(
            group_identifier=self.object.group_identifier)
        return options

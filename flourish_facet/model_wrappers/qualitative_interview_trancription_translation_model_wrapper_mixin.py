from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .qualitative_interview_trancription_translation_model_wrapper import QualitativeInterviewTranscriptionAndTranslationModelWrapper


class QualitativeInterviewTranscriptionAndTranslationModelWrapperMixin:

    qualitative_interview_transcription_translation_model_wrapper_cls = QualitativeInterviewTranscriptionAndTranslationModelWrapper

    @property
    def qualitative_interview_transcription_translation_model_obj(self):
        """Returns a qualitative interview transcription and translation instance or None.
        """
        try:
            return self.qualitative_interview_transcription_translation_cls.objects.get(
                **self.qualitative_interview_transcription_translation_options)
        except ObjectDoesNotExist:
            return None

    @property
    def qualitative_interview_transcription_translation(self):
        """Returns a wrapped unsaved qualitative interview transcription and translation.
        """
        model_obj = self.qualitative_interview_transcription_translation_model_obj or \
            self.qualitative_interview_transcription_translation_cls(
                **self.create_qualitative_interview_transcription_translation_options)
        return self.qualitative_interview_transcription_translation_model_wrapper_cls(model_obj=model_obj)

    @property
    def qualitative_interview_transcription_translation_cls(self):
        return django_apps.get_model('flourish_facet.qualitativeinterviewtranscriptionandtranslation')

    @property
    def create_qualitative_interview_transcription_translation_options(self):
        """Returns a dictionary of options to create a new
        unpersisted qualitative interview transcription and translation model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

    @property
    def qualitative_interview_transcription_translation_options(self):
        """Returns a dictionary of options to get an existing
        qualitative interview transcription and translation model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

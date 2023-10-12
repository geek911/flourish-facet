from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .qualitative_interview_audio_upload_model_wrapper import QualitativeInterviewAudioUploadModelWrapper


class QualitativeInterviewAudioUploadModelWrapperMixin:

    qualitative_interview_audio_upload_model_wrapper_cls = QualitativeInterviewAudioUploadModelWrapper

    @property
    def qualitative_interview_audio_upload_model_obj(self):
        """Returns a qualitative interview audio upload instance or None.
        """
        try:
            return self.qualitative_interview_audio_upload_cls.objects.get(
                **self.qualitative_interview_audio_upload_options)
        except ObjectDoesNotExist:
            return None

    @property
    def qualitative_interview_audio_upload(self):
        """Returns a wrapped unsaved qualitative interview audio upload.
        """
        model_obj = self.qualitative_interview_audio_upload_model_obj or \
            self.qualitative_interview_audio_upload_cls(
                **self.create_qualitative_interview_audio_upload_options)
        return self.qualitative_interview_audio_upload_model_wrapper_cls(model_obj=model_obj)

    @property
    def qualitative_interview_audio_upload_cls(self):
        return django_apps.get_model('flourish_facet.qualitativeinterviewaudiouploads')

    @property
    def create_qualitative_interview_audio_upload_options(self):
        """Returns a dictionary of options to create a new
        unpersisted qualitative interview audio upload model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

    @property
    def qualitative_interview_audio_upload_options(self):
        """Returns a dictionary of options to get an existing
        qualitative interview audio upload model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

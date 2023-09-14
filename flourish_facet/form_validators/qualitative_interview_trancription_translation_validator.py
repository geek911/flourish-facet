from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class QualitativeInterviewTranscriptionAndTranslationFormValidator(FormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')
        super().clean()
        self.validate_trancription_incomplete(cleaned_data=self.cleaned_data)
        self.validate_translation_incomplete(
            cleaned_data=self.cleaned_data)

    def validate_trancription_incomplete(self, cleaned_data=None):
        transcription_upload = cleaned_data.get('transcription_upload')
        complete = cleaned_data.get('complete')

        if transcription_upload == NO and complete == 'Complete':
            raise ValidationError("You’ve indicated that the transcription was not uploaded"
                                  "to Dropbox. Please save the form as incomplete"
                                  "When the transcription is uploaded to Dropbox"
                                  "return to this form and save the form as “complete")

    def validate_translation_incomplete(self, cleaned_data=None):
        translation_upload = cleaned_data.get('translation_upload')
        complete = cleaned_data.get('complete')

        if translation_upload == NO and complete == 'Complete':
            raise ValidationError("You’ve indicated that the translation was not uploaded"
                                  "to Dropbox. Please save the form as incomplete"
                                  "When the translation is uploaded to Dropbox"
                                  "return to this form and save the form as “complete")

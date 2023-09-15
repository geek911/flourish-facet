from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class QualitativeInterviewAudioUploadsFormValidator(FormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')
        super().clean()
        self.validate_audio_file_not_uploaded(cleaned_data=self.cleaned_data)
        self.validate_audio_file_uploaded(cleaned_data=self.cleaned_data)

        self.validate_other_specify(
            field='location', other_specify_field='location_other')

    def validate_audio_file_not_uploaded(self, cleaned_data=None):
        audio_file = cleaned_data.get('audio_file')
        complete = cleaned_data.get('complete')

        if audio_file == NO and complete == 'complete':
            raise ValidationError("You’ve indicated that the audio file was not uploaded to"
                                  "Dropbox. Please save the form as incomplete. When the audio file is uploaded to Dropbox,"
                                  "please respond “Yes” to the above question and save the form as complete.")

    def validate_audio_file_uploaded(self, cleaned_data=None):
        audio_file = cleaned_data.get('audio_file')
        complete = cleaned_data.get('complete')

        if audio_file == YES and complete == 'unverified':
            raise ValidationError(
                "You’ve indicated that the audio file was uploaded, save the form as complete.")

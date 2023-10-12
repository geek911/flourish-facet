from edc_form_validators import FormValidator


class QualitativeInterviewAudioUploadsFormValidator(FormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')
        super().clean()
        self.validate_other_specify(
            field='location', other_specify_field='location_other')

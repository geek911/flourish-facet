from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class QualitativeInterviewAudioUploadsFormValidator(FormValidator):

    def clean(self):
        super().clean()
        self.validate_other_specify(
            field='location', other_specify_field='location_other')

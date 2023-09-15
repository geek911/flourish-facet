from django.test import TestCase
from ..form_validators import QualitativeInterviewAudioUploadsFormValidator
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class TestQualitativeInterviewAudioUploadsForm(TestCase):

    def test_audio_uploaded_invalid(self):
        cleaned_data = {
            'audio_file': NO,
            'complete': 'Complete'
        }
        form_validator = QualitativeInterviewAudioUploadsFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_audio_uploaded_invalid_unverified(self):
        cleaned_data = {
            'audio_file': YES,
            'complete': 'Unverified'
        }
        form_validator = QualitativeInterviewAudioUploadsFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

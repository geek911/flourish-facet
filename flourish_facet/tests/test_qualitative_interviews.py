from django.test import TestCase, tag
from ..form_validators import (QualitativeInterviewAudioUploadsFormValidator,
                               QualitativeInterviewTranscriptionAndTranslationFormValidator,
                               QualitativeInterviewSchedulingFormValidator)
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class TestQualitativeInterviewForms(TestCase):

    @tag('audio_upload')
    def test_audio_uploaded_invalid(self):
        cleaned_data = {
            'audio_file': NO,
            'complete': 'complete'
        }
        form_validator = QualitativeInterviewAudioUploadsFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_audio_uploaded_invalid_unverified(self):
        cleaned_data = {
            'audio_file': YES,
            'complete': 'unverified'
        }
        form_validator = QualitativeInterviewAudioUploadsFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    @tag('scheduling')
    def test_google_calendar_sheet_complete(self):
        cleaned_data = {
            'google_sheet_calendar': YES,
            'facet_consent_form': YES,
            'complete': 'incomplete'
        }
        form_validator = QualitativeInterviewSchedulingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_google_calendar_sheet_incomplete(self):
        cleaned_data = {
            'google_sheet_calendar': NO,
            'complete': 'complete'
        }
        form_validator = QualitativeInterviewSchedulingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_google_calendar_sheet_unverified(self):
        cleaned_data = {
            'google_sheet_calendar': YES,
            'facet_consent_form': YES,
            'complete': 'unverified'
        }
        form_validator = QualitativeInterviewSchedulingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_facet_consent_form_incomplete(self):
        cleaned_data = {
            'facet_consent_form': NO,
            'complete': 'complete'
        }
        form_validator = QualitativeInterviewSchedulingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    @tag('transcription_translation')
    def test_transcription_incomplete(self):
        cleaned_data = {
            'transcription_upload': NO,
            'complete': 'complete'
        }
        form_validator = QualitativeInterviewTranscriptionAndTranslationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_translation_incomplete(self):
        cleaned_data = {
            'translation_upload': NO,
            'complete': 'complete'
        }
        form_validator = QualitativeInterviewTranscriptionAndTranslationFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

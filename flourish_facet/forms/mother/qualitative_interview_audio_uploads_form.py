from django import forms
from flourish_facet.form_validators.qualitative_interview_audio_uploads_validation import QualitativeInterviewAudioUploadsFormValidator
from ...models import QualitativeInterviewAudioUploads
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


class QualitativeInterviewAudioUploadsForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = QualitativeInterviewAudioUploadsFormValidator

    class Meta:
        model = QualitativeInterviewAudioUploads
        fields = '__all__'

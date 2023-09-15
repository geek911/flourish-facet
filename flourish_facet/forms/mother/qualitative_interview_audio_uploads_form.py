from django import forms
from flourish_facet.form_validators.qualitative_interview_audio_uploads_validation import QualitativeInterviewAudioUploadsFormValidator
from ...models import QualitativeInterviewAudioUploads
from edc_base.sites import SiteModelFormMixin


class QualitativeInterviewAudioUploadsForm(SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = QualitativeInterviewAudioUploadsFormValidator

    class Meta:
        model = QualitativeInterviewAudioUploads
        fields = '__all__'

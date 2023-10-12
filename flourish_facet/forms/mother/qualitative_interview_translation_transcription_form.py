from django import forms
from ...models import QualitativeInterviewTranscriptionAndTranslation
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


class QualitativeInterviewTranscriptionAndTranslationForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = QualitativeInterviewTranscriptionAndTranslation
        fields = '__all__'

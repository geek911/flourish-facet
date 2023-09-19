from django import forms
from flourish_facet.form_validators import QualitativeInterviewTranscriptionAndTranslationFormValidator
from ...models import QualitativeInterviewTranscriptionAndTranslation
from edc_base.sites import SiteModelFormMixin


class QualitativeInterviewTranscriptionAndTranslationForm(SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = QualitativeInterviewTranscriptionAndTranslationFormValidator

    class Meta:
        model = QualitativeInterviewTranscriptionAndTranslation
        fields = '__all__'

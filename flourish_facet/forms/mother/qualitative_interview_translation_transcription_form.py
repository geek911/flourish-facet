from django import forms
from ...models import QualitativeInterviewTranscriptionAndTranslation
from edc_base.sites import SiteModelFormMixin


class QualitativeInterviewTranscriptionAndTranslationForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = QualitativeInterviewTranscriptionAndTranslation
        fields = '__all__'

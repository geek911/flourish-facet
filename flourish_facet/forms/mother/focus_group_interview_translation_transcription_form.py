from django import forms
from ...models import FocusGroupInterviewTranscriptionAndTranslation
from edc_base.sites import SiteModelFormMixin
from django.apps import apps as django_apps


class FocusGroupInterviewTranscriptionAndTranslationForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = FocusGroupInterviewTranscriptionAndTranslation
        fields = '__all__'

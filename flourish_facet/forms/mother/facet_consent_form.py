from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin
from ...models.mother import FacetConsent
from ...form_validators import FacetConsentFormValidator
from django.core.exceptions import ValidationError


class FacetConsentForm(FormValidatorMixin,
                       forms.ModelForm):
    form_validator_cls = FacetConsentFormValidator

    subject_identifier = forms.CharField(
        label='Facet Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = FacetConsent
        fields = '__all__'

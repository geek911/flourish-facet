from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin
from ...models.mother import FacetConsent


class FacetConsentForm(FormValidatorMixin, ConsentModelFormMixin,
                       forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = FacetConsent
        fields = '__all__'

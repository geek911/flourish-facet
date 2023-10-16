from django import forms
from ...models import MotherChildConsent
from edc_form_validators import FormValidatorMixin


class MotherChildConsentForm(FormValidatorMixin, forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = MotherChildConsent
        fields = '__all__'

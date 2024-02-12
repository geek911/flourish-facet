from django import forms
from edc_form_validators import FormValidatorMixin
from flourish_facet.form_validators import FacetContactFormValidator

from ..models import FacetContact


class FacetContactForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = FacetContactFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = FacetContact
        fields = '__all__'

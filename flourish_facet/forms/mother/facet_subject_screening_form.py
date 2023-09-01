from django import forms
from ...models.mother import FacetSubjectScreening
from ...form_validators import FacetSubjectScreeningValidator
from edc_form_validators import FormValidatorMixin


class FacetSubjectScreeningForm(FormValidatorMixin,forms.ModelForm):
    form_validator_cls = FacetSubjectScreeningValidator

    class Meta:
        model = FacetSubjectScreening
        fields = '__all__'

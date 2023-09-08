from django import forms
from ...models.mother import FacetSubjectScreening
from ...form_validators import FacetSubjectScreeningValidator


class FacetSubjectScreeningForm(forms.ModelForm):
    
    form_validator_cls = FacetSubjectScreeningValidator

    class Meta:
        model = FacetSubjectScreening
        fields = '__all__'

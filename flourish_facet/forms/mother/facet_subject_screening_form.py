from django import forms
from ...models.mother import FacetSubjectScreening


class FacetSubjectScreeningForm(forms.ModelForm):

    class Meta:
        model = FacetSubjectScreening
        fields = '__all__'

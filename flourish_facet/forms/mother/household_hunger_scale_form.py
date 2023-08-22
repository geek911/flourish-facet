from django import forms
from ...models import HouseholdHungerScale


class HouseholdHungerScaleForm(forms.ModelForm):

    class Meta:
        model = HouseholdHungerScale
        fields = '__all__'

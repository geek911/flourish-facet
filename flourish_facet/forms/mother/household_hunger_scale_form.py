from django import forms
from ...models import HouseholdHungerScale
from edc_base.sites import SiteModelFormMixin


class HouseholdHungerScaleForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = HouseholdHungerScale
        fields = '__all__'

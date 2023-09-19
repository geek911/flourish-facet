from django import forms
from ...models import HouseholdHungerScale
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


class HouseholdHungerScaleForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = HouseholdHungerScale
        fields = '__all__'

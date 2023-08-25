from django import forms
from ...models import ChildHivTesting
from edc_base.sites import SiteModelFormMixin
from ...form_validators import ChildHivTestingFormValidator


class ChildHivTestingForm(SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = ChildHivTestingFormValidator

    class Meta:
        model = ChildHivTesting
        fields = '__all__'

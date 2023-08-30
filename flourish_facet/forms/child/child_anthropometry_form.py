from django import forms
from ...models import ChildAnthropometry
from ...form_validators import ChildAnthropometryFormValidator
from edc_base.sites import SiteModelFormMixin


class ChildAnthropometryForm(SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = ChildAnthropometryFormValidator

    class Meta:
        model = ChildAnthropometry
        fields = '__all__'

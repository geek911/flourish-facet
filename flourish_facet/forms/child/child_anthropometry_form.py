from django import forms
from ...models import ChildAnthropometry
from ...form_validators import ChildAnthropometryFormValidator


class ChildAnthropometryForm(forms.ModelForm):

    form_validator_cls = ChildAnthropometryFormValidator

    class Meta:
        model = ChildAnthropometry
        fields = '__all__'

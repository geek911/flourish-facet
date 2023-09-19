from django import forms
from ...models import IntimatePartnerViolence
from edc_form_validators import FormValidatorMixin


class IntimatePartnerViolenceForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = IntimatePartnerViolence
        fields = '__all__'

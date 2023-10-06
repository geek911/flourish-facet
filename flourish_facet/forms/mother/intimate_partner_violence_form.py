from django import forms
from ...models import IntimatePartnerViolence
from ...form_validators import IntimatePartnerViolenceFormValidator
from edc_form_validators import FormValidatorMixin
from edc_base.sites import SiteModelFormMixin


class IntimatePartnerViolenceForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = IntimatePartnerViolenceFormValidator

    class Meta:
        model = IntimatePartnerViolence
        fields = '__all__'

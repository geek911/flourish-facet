from django import forms
from ...models import IntimatePartnerViolence
from edc_form_validators import FormValidatorMixin
from edc_base.sites import SiteModelFormMixin


class IntimatePartnerViolenceForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = IntimatePartnerViolence
        fields = '__all__'

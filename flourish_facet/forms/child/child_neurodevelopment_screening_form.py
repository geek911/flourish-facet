from django import forms
from ...models import ChildNeurodevelopmentScreening
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


class ChildNeurodevelopmentScreeningForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ChildNeurodevelopmentScreening
        fields = '__all__'

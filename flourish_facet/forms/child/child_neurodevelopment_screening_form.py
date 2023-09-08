from django import forms
from ...models import ChildNeurodevelopmentScreening
from edc_base.sites import SiteModelFormMixin


class ChildNeurodevelopmentScreeningForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ChildNeurodevelopmentScreening
        fields = '__all__'

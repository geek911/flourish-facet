from django import forms
from ...models import ChildHivTesting
from edc_base.sites import SiteModelFormMixin


class ChildHivTestingForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ChildHivTesting
        fields = '__all__'

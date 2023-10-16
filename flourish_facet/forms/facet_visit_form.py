from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from ..models import FacetVisit


class FacetVisitForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = FacetVisit
        fields = '__all__'

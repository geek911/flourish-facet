from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from ..models import Appointment


class FacetAppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'

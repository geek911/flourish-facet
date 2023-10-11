from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from .form_mixins import SubjectModelFormMixin
from ..models import FacetClinicianNotes, FacetClinicianNotesImage


class FacetClinicianNotesForm(SubjectModelFormMixin,):
    class Meta:
        model = FacetClinicianNotes
        fields = '__all__'


class FacetClinicianNotesImageForm(forms.ModelForm):
    class Meta:
        model = FacetClinicianNotesImage
        fields = '__all__'


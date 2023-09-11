from django import forms
from django.db.models import ManyToManyField
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from ...form_validators import SocioDemographicDataFormValidator
from itertools import chain
from ...models import FacetSocioDemographicData
from ..form_mixins import SubjectModelFormMixin


class FacetSocioDemographicDataForm(SubjectModelFormMixin, forms.ModelForm):
    form_validator_cls = SocioDemographicDataFormValidator

    class Meta:
        model = FacetSocioDemographicData
        fields = '__all__'

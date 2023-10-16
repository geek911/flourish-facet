from django import forms
from django.db.models import ManyToManyField
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from ...form_validators import ChildSocioDemographicFormValidator
from itertools import chain
from ...models import FacetChildSocioDemographic
from ..form_mixins import SubjectModelFormMixin


class ChildSocioDemographicForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = ChildSocioDemographicFormValidator

    class Meta:
        model = FacetChildSocioDemographic
        fields = '__all__'

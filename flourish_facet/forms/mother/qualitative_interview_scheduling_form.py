from django import forms
from flourish_facet.form_validators import QualitativeInterviewSchedulingFormValidator
from ...models import QualitativeInterviewScheduling
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


class QualitativeInterviewSchedulingForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = QualitativeInterviewSchedulingFormValidator

    class Meta:
        model = QualitativeInterviewScheduling
        fields = '__all__'

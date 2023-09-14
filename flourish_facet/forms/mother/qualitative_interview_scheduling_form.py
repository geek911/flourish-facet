from django import forms
from flourish_facet.form_validators import QualitativeInterviewSchedulingFormValidator
from ...models import QualitativeInterviewScheduling
from edc_base.sites import SiteModelFormMixin


class QualitativeInterviewSchedulingForm(SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = QualitativeInterviewSchedulingFormValidator

    class Meta:
        model = QualitativeInterviewScheduling
        fields = '__all__'

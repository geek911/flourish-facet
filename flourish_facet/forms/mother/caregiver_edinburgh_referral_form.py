from flourish_caregiver.forms.form_mixins import SubjectModelFormMixin
from ...models import FacetCaregiverEdinburghReferral

from flourish_form_validations.form_validators import CaregiverReferralFormValidator


class FacetCaregiverEdinburghReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFormValidator

    class Meta:
        model = FacetCaregiverEdinburghReferral
        fields = '__all__'

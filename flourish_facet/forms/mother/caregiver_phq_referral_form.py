from flourish_caregiver.forms.form_mixins import SubjectModelFormMixin
from ...models import FacetCaregiverPhqReferral

from flourish_form_validations.form_validators import CaregiverReferralFormValidator


class FacetCaregiverPhqReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFormValidator

    class Meta:
        model = FacetCaregiverPhqReferral
        fields = '__all__'

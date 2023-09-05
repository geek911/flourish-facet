from flourish_form_validations.form_validators import CaregiverReferralFUFormValidator

from ...models import FacetCaregiverGadPostReferral
from flourish_caregiver.forms.form_mixins import SubjectModelFormMixin


class FacetCaregiverGadPostReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFUFormValidator

    class Meta:
        model = FacetCaregiverGadPostReferral
        fields = '__all__'

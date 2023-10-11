from flourish_facet.forms.form_mixins import SubjectModelFormMixin
from ...models import IntimatePartnerViolenceReferral
from ...form_validators import CaregiverReferralFormValidator


class IntimatePartnerViolenceReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFormValidator

    class Meta:
        model = IntimatePartnerViolenceReferral
        fields = '__all__'

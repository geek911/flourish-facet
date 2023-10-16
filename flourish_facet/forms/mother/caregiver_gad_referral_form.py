from flourish_facet.forms.form_mixins import SubjectModelFormMixin
from ...models import FacetCaregiverGadReferral
from ...form_validators import CaregiverReferralFormValidator


class FacetCaregiverGadReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFormValidator

    class Meta:
        model = FacetCaregiverGadReferral
        fields = '__all__'

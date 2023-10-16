from ...form_validators import CaregiverReferralFUFormValidator
from ...models import FacetCaregiverPhqPostReferral
from flourish_facet.forms.form_mixins import SubjectModelFormMixin


class FacetCaregiverPhqPostReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFUFormValidator

    class Meta:
        model = FacetCaregiverPhqPostReferral
        fields = '__all__'

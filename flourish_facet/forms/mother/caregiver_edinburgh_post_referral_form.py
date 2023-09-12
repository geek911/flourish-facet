from ...form_validators import CaregiverReferralFUFormValidator
from ...models import FacetCaregiverEdinburghPostReferral
from flourish_facet.forms.form_mixins import SubjectModelFormMixin


class FacetCaregiverEdinburghPostReferralForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFUFormValidator

    class Meta:
        model = FacetCaregiverEdinburghPostReferral
        fields = '__all__'

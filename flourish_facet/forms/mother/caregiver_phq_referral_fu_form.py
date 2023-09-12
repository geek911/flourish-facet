from ...form_validators import CaregiverReferralFUFormValidator

from ...models import FacetCaregiverPhqReferralFU
from flourish_caregiver.forms.form_mixins import SubjectModelFormMixin


class FacetCaregiverPhqReferralFUForm(SubjectModelFormMixin):

    form_validator_cls = CaregiverReferralFUFormValidator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['emo_support_type'].label = ('4. What kind of emotional support are you '
                                                 'receiving?')

    class Meta:
        model = FacetCaregiverPhqReferralFU
        fields = '__all__'

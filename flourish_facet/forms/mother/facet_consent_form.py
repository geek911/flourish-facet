from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin
from ...models.mother import FacetConsent
from ...form_validators import FacetConsentFormValidator
from django.core.exceptions import ValidationError
from edc_constants.constants import NO, YES


class FacetConsentForm(FormValidatorMixin,
                       forms.ModelForm):
    form_validator_cls = FacetConsentFormValidator

    subject_identifier = forms.CharField(
        label='Facet Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        child_consent = cleaned_data.get('child_consent')
        mother_child_consent = self.data.get(
            'motherchildconsent_set-TOTAL_FORMS')

        if child_consent == NO and int(mother_child_consent) != 0:
            msg = {'child_consent':
                   'Participant is not willing to consent on behalf of child.'
                   'Caregiver child consent should not be completed. To proceed,'
                   ' close Caregiver Child Consent.'}

            raise forms.ValidationError(msg)
        elif child_consent == YES and int(mother_child_consent) == 0:

            raise forms.ValidationError('Please complete the Caregiver '
                                        'consent for child participation')

    class Meta:
        model = FacetConsent
        fields = '__all__'

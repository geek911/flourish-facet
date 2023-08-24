from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin
from ...models.mother import FacetConsent
from ...form_validators import FacetConsentFormValidator
from django.core.exceptions import ValidationError


class FacetConsentForm(FormValidatorMixin, ConsentModelFormMixin,
                       forms.ModelForm):
    form_validator_cls = FacetConsentFormValidator

    subject_identifier = forms.CharField(
        label='Facet Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    def clean(self):
        """
        Raise ValidationError if least one child consent inline form is not added.
        """
        clean_data = super().clean()

        child_consent_inlines = int(
            self.data.get('flourish_facetmotherchildconsent_set-TOTAL_FORMS', 0))

        if child_consent_inlines == 0:
            raise ValidationError('You must add at least one child consent')
        return clean_data

    class Meta:
        model = FacetConsent
        fields = '__all__'

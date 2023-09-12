from django import forms
from django.apps import apps as django_apps
from flourish_form_validations.form_validators import FormValidatorMixin as FlourishFormValidatorMixin


class FormValidatorMixin(FlourishFormValidatorMixin):
    facet_consent_model = 'flourish_facet.facetconsent'

    @property
    def facet_consent_cls(self):
        return django_apps.get_model(self.facet_consent_model)

    def clean(self):
        if self.cleaned_data.get('facet_visit', None):
            self.subject_identifier = self.cleaned_data.get(
                'facet_visit').subject_identifier
            self.validate_against_visit_datetime(
                self.cleaned_data.get('report_datetime'))
        else:
            self.subject_identifier = self.cleaned_data.get(
                'subject_identifier')
        super().clean()

    @property
    def latest_consent_obj(self):

        facet_consents = self.facet_consent_cls.objects.filter(
            subject_identifier=self.subject_identifier)

        if facet_consents:
            return facet_consents.latest('consent_datetime')

    def validate_against_visit_datetime(self, report_datetime):
        if (report_datetime and report_datetime <
                self.cleaned_data.get('facet_visit').report_datetime):
            raise forms.ValidationError(
                "Report datetime cannot be before visit datetime.")

from edc_form_validators import FormValidator
from edc_constants.constants import NO
from django.apps import apps as django_apps
from django.forms import ValidationError


class FacetSubjectScreeningValidator(FormValidator):

    flourish_consent_model = 'flourish_caregiver.subjectconsent'

    @property
    def flourish_consent_cls(self):
        return django_apps.get_model(self.flourish_consent_model)

    def clean(self):
        super().clean()

        self.consent_exist_validations()

        self.required_if(NO, field='facet_participation',
                         field_required='reasons_unwilling_part')

        self.validate_other_specify(
            field='reasons_unwilling_part',
            other_specify_field='reasons_unwilling_part_other')

    def consent_exist_validations(self):
        subject_identifier = self.cleaned_data.get('')

        consent_exists = self.flourish_consent_cls.objects.filter(
            subject_identifier=subject_identifier).exists()

        if not consent_exists:
            raise ValidationError(
                {'subject_identifier': 'Subject identifier does not exist in Flourish'})

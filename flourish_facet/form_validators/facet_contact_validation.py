from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator

from .crf_form_validator import FormValidatorMixin


class FacetContactFormValidator(FormValidatorMixin, FormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')

        self.validate_against_consent_datetime(self.cleaned_data.get('report_datetime'))

        self.required_if(
            YES,
            field='contact_success',
            field_required='contact_comment',
            inverse=False)

        self.validate_other_specify(
            field='reason_rescheduled',
            other_specify_field='reason_rescheduled_other',
        )

        self.required_if(
            YES,
            field='call_rescheduled',
            field_required='reason_rescheduled',
        )

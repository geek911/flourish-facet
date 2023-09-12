from edc_form_validators import FormValidator
from django.core.exceptions import ValidationError
from django import forms
from edc_constants.constants import NO
import re


class FacetConsentFormValidator(FormValidator):
    facet_consent_model = 'flourish_facet.facetconsent'

    def clean(self):
        self.clean_full_name_syntax()
        self.clean_initials_with_full_name()
        self.required_if(NO, field='is_literate', field_required='witness_name' )
        

    def clean_full_name_syntax(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and not re.match(r'^[A-Z]+$|^([A-Z]+[ ][A-Z]+)$', first_name):
            message = {'first_name': 'Ensure first name is letters (A-Z) in '
                                     'upper case, no special characters, except spaces. '
                                     'Maximum 2 first '
                                     'names allowed.'}
            self._errors.update(message)
            raise ValidationError(message)

        if last_name and not re.match(r'^[A-Z-]+$', last_name):
            message = {'last_name': 'Ensure last name is letters (A-Z) in '
                                    'upper case, no special characters, except hyphens.'}
            self._errors.update(message)
            raise ValidationError(message)

        if first_name and first_name != first_name.upper():
            message = {'first_name': 'First name must be in CAPS.'}
            self._errors.update(message)
            raise ValidationError(message)
        if last_name and last_name != last_name.upper():
            message = {'last_name': 'Last name must be in CAPS.'}
            self._errors.update(message)
            raise ValidationError(message)

    def clean_initials_with_full_name(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        initials = cleaned_data.get("initials")
        try:
            middle_name = None
            is_first_name = False
            new_first_name = None
            if first_name and len(first_name.split(' ')) > 1:
                new_first_name = first_name.split(' ')[0]
                middle_name = first_name.split(' ')[1]

            if middle_name and (middle_name and
                                (initials[:1] != new_first_name[:1] or
                                 initials[1:2] != middle_name[:1])):
                is_first_name = True

            elif not middle_name and initials[:1] != first_name[:1]:
                is_first_name = True

            if is_first_name or initials[-1:] != last_name[:1]:
                raise forms.ValidationError(
                    {'initials': 'Initials do not match full name.'},
                    params={
                        'initials': initials,
                        'first_name': first_name,
                        'last_name': last_name},
                    code='invalid')
        except (IndexError, TypeError):
            raise forms.ValidationError('Initials do not match fullname.')

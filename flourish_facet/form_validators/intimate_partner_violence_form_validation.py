from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES
from edc_constants.choices import NOT_APPLICABLE
from django.core.exceptions import ValidationError


class IntimatePartnerViolenceFormValidator(FormValidator):
    def clean(self):

        super().clean()
        self.validate_violence(cleaned_data=self.cleaned_data)

    def validate_violence(self, cleaned_data=None):

        physically_hurt = cleaned_data.get('physically_hurt')
        insult_talk = cleaned_data.get('insult_talk')
        threaten = cleaned_data.get('threaten')
        scream_curse = cleaned_data.get('scream_curse')

        self.applicable_if_true(
            physically_hurt in ['rarely', 'sometimes', 'fairly_often', 'frequently'
                                ] or insult_talk in ['rarely', 'sometimes', 'fairly_often', 'frequently'
                                                     ] or threaten in ['rarely', 'sometimes', 'fairly_often', 'frequently'] or scream_curse in ['rarely', 'sometimes', 'fairly_often', 'frequently'],
            field_applicable='referral')

from edc_form_validators import FormValidator
from edc_constants.choices import NOT_APPLICABLE


class IntimatePartnerViolenceFormValidator(FormValidator):
    def clean(self):

        super().clean()
        self.validate_violence(cleaned_data=self.cleaned_data)

    def validate_violence(self, cleaned_data=None):
        responses = ['never', NOT_APPLICABLE]
        physically_hurt = cleaned_data.get('physically_hurt')
        insult_talk = cleaned_data.get('insult_talk')
        threaten = cleaned_data.get('threaten')
        scream_curse = cleaned_data.get('scream_curse')
        not_applicable = all([physically_hurt in responses, insult_talk in responses,
                             threaten in responses, scream_curse in responses])

        self.applicable_if_true(
            not not_applicable,
            field_applicable='referral')

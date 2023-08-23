from edc_form_validators import FormValidator


class ChildHivTestingFormValidator(FormValidator):
    def clean(self):
        form = 'validators'

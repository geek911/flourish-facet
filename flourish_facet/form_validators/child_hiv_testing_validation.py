from edc_form_validators import FormValidator
from edc_constants.constants import NO


class ChildHivTestingFormValidator(FormValidator):
    def clean(self):

        self.required_if(NO, field='child_tested',
                         field_required='reason_not_tested')

        self.required_if(NO, field='child_tested_6_weeks',
                         field_required='reason_not_tested_6_weeks')

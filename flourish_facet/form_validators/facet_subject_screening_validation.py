from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES


class FacetSubjectScreeningValidator(FormValidator):
    def clean(self):
        super().clean()

        self.required_if(NO, field='facet_participation',
                         field_required='reasons_unwilling_part')

        self.validate_other_specify(
            field='reasons_unwilling_part',
            other_specify_field='reasons_unwilling_part_other')

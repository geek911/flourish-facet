from edc_form_validators import FormValidator
from edc_constants.constants import NO


class MaternalHivArtFormValidator(FormValidator):
    def clean(self):

        self.validate_other_specify(
            field='drug_combination_before', other_specify_field='drug_combination_before_other')

        self.validate_other_specify(
            field='drug_combination_during', other_specify_field='drug_combination_during_other')

        self.validate_other_specify(
            field='art_regimen', other_specify_field='art_regimen_other')

        self.validate_other_specify(
            field='reason_regimen_change', other_specify_field='reason_regimen_change_other')

        self.validate_other_specify(
            field='art_challenges', other_specify_field='art_challenges_other')

        self.not_required_if(NO, field='father_hiv',
                             field_required='father_hiv_dont')
        self.not_required_if('Dont_know', field='father_hiv',
                             field_required='father_hiv_no')

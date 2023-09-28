from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES
from django.core.exceptions import ValidationError


class MaternalHivArtFormValidator(FormValidator):
    def clean(self):
        super().clean()

        self.date_not_before_date_for_positive(cleaned_data=self.cleaned_data)
        self.date_previous_not_before_art_start(cleaned_data=self.cleaned_data)
        self.validate_art_received(cleaned_data=self.cleaned_data)
        self.date_not_before_hiv_date_father(cleaned_data=self.cleaned_data)

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

        self.required_if(YES, field='art_received',
                         field_required='drug_combination_before')

        self.required_if(YES, field='art_received_preg',
                         field_required='drug_combination_during')
        required_art_regimen_list = [
            'art_regimen', 'art_regimen_start', 'reason_regimen_change']

        for art_regimen in required_art_regimen_list:
            self.required_if(
                YES,
                field='art_switch',
                field_required=art_regimen,
                required_msg='If Art regimen was switched, this field is required.')

        self.required_if(NO, field='father_hiv',
                         field_required='father_hiv_no')

        self.required_if('Dont_know', field='father_hiv',
                         field_required='father_hiv_dont')

        father_hiv_details_list = ['hiv_result_father', 'hiv_test_date_father']

        for father_hiv_details in father_hiv_details_list:
            self.required_if(
                YES,
                field='father_no',
                field_required=father_hiv_details,
                required_msg='If Father was tested, this field is required.')

        self.required_if(YES, field='father_art',
                         field_required='father_art_start')

        self.required_if(YES, field='hiv_status_disclosure',
                         field_required='hiv_status_disclosure_reaction')

    def validate_art_received(self, cleaned_data=None):
        art_received = cleaned_data.get('art_received')
        art_received_preg = cleaned_data.get('art_received_preg')

        self.required_if_true(
            art_received == YES or art_received_preg == YES,
            field_required='art_challenges')

    def date_not_before_date_for_positive(self, cleaned_data=None):
        date_tested_positive = cleaned_data.get('hiv_test_date')
        art_start_date = cleaned_data.get('art_start_date')
        if date_tested_positive and art_start_date:
            if art_start_date < date_tested_positive:
                raise ValidationError(
                    'Art start date cannot be a date before the date participant tested positive')

    def date_previous_not_before_art_start(self, cleaned_data=None):
        art_regimen_start = cleaned_data.get('art_regimen_start')
        art_start_date = cleaned_data.get('art_start_date')

        if art_regimen_start and art_start_date:
            if art_regimen_start < art_start_date:
                raise ValidationError(
                    'Art previous regimen start date cannot be a date before the Art start date')

    def date_not_before_hiv_date_father(self, cleaned_data=None):
        date_tested = cleaned_data.get('hiv_test_date_father')
        father_art_start_date = cleaned_data.get('father_art_start')
        if date_tested and father_art_start_date:
            if father_art_start_date < date_tested:
                raise ValidationError(
                    'Father Art start date cannot be a date before the date Father tested for Hiv')

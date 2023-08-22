from edc_form_validators import FormValidator


class ChildAnthropometryFormValidator(FormValidator):
    def clean(self):

        self.applicable_if_true(
            self.calculate_weight_diff >= 0.10,
            field_applicable='weight_3'
        )
        self.applicable_if_true(
            self.calculate_length_diff >= 0.5,
            field_applicable='length_3'
        )

    @property
    def calculate_weight_diff(self, cleaned_data=None):
        weight_1 = cleaned_data.get(weight_1)
        weight_2 = cleaned_data.get(weight_2)

        return weight_1 - weight_2

    @property
    def calculate_length_diff(self, cleaned_data=None):
        length_1 = cleaned_data.get(length_1)
        length_2 = cleaned_data.get(length_2)

        return length_1 - length_2

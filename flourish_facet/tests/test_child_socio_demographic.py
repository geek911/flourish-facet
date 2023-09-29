import unittest

from django.core.exceptions import ValidationError
from django.test import tag

from flourish_facet.form_validators import ChildSocioDemographicFormValidator


@tag('child_socio_demographic')
class TestChildSocioDemographic(unittest.TestCase):

    def setUp(self):
        self.data = {'older_than18': None, 'house_people_number': None}

    def test_validate_more_than_total(self):
        self.data['older_than18'] = 5
        self.data['house_people_number'] = 4

        form_validator = ChildSocioDemographicFormValidator(
            cleaned_data=self.data
        )

        with self.assertRaises(ValidationError):
            form_validator.validate_number_of_people_living_in_the_household()
        self.assertIn('older_than18', form_validator._errors)

    def test_validate_same_as_total(self):
        self.data['older_than18'] = 4
        self.data['house_people_number'] = 4

        form_validator = ChildSocioDemographicFormValidator(
            cleaned_data=self.data
        )

        with self.assertRaises(ValidationError):
            form_validator.validate_number_of_people_living_in_the_household()
        self.assertIn('older_than18', form_validator._errors)

    def test_validate_less_than_total(self):
        self.data['older_than18'] = 2
        self.data['house_people_number'] = 4

        form_validator = ChildSocioDemographicFormValidator(
            cleaned_data=self.data
        )

        form_validator.validate_number_of_people_living_in_the_household()
        self.assertNotIn('older_than18', form_validator._errors)

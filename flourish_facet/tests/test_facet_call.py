from django.test import TestCase, tag
from django.utils import timezone
from flourish_facet import models
from ..form_validators import FacetContactFormValidator
from django.core.exceptions import ValidationError


@tag('fcc')
class FacetContactModelTestCase(TestCase):

    def setUp(self):
        self.facet_contact_data = {
            'report_datetime': timezone.now(),
            'contact_type': 'test',
            'contact_datetime': timezone.now(),
            'call_reason': 'test',
            'contact_success': 'YES',
        }

    def test_facet_contact_creation(self):
        # Test facet_contact with correct options data
        facet_contact = models.FacetContact.objects.create(
            **self.facet_contact_data)
        msg = "Test object is none."
        self.assertIsNotNone(facet_contact, msg)

        self.assertEqual(facet_contact.contact_success,
                         self.facet_contact_data['contact_success'])

    def test_facet_contact_with_invalid_data(self):
        # Test facet_contact with invalid data
        cleaned_data = {
            'report_datetime': None,
            'contact_type': 'test',
            'contact_datetime': timezone.now(),
            'call_reason': 'test',
            'contact_success': 'YES',
        }

        form_validator = FacetContactFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)

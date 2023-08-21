from django.test import TestCase
from edc_constants.constants import NO, YES
from ..models.mother.eligibility import FacetEligibility


class TestEligibility(TestCase):
    def test_facet_participation_ineligible(self):
        eligibility = FacetEligibility(
            facet_participation=NO,
        )
        self.assertFalse(eligibility.is_eligible)
        self.assertIn(
            'Not interested in participating in the Facet study', eligibility.error_message)

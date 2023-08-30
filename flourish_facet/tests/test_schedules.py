from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES
from ..models.mother.eligibility import FacetEligibility
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from ..models import OnScheduleFacetChild, OnScheduleFacetMother

class TestSchedule(TestCase):

    def setUp(self) -> None:
        self.subject_identifier = '1234567890'

    @tag('ttt')
    def test_put_mother_onschedule(self):


        schedule_name = 'mother_facet_schedule'



        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model=OnScheduleFacetMother, name=schedule_name
        )

        schedule.put_on_schedule(
            subject_identifier=self.subject_identifier,
                onschedule_datetime=get_utcnow(),
                schedule_name=schedule_name,
                base_appt_datetime=get_utcnow()
        )
    def test_facet_participation_ineligible(self):
        eligibility = FacetEligibility(
            facet_participation=NO,
        )
        self.assertFalse(eligibility.is_eligible)
        self.assertIn(
            'Not interested in participating in the Facet study', eligibility.error_message)

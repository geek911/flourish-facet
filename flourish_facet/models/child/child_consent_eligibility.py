from edc_constants.constants import NO
from datetime import date
from edc_base.utils import age


class ChildConsentEligibility:
    def __init__(self, child_dob: date, child_test, consent_date: date):

        self.error_message = []

        child_age = age(child_dob, consent_date)

        if child_age.years == 0 and not (0 <= child_age.months <= 6):
            self.error_message.append('Age not withing range')

        if child_test == NO:
            self.error_message.append('Child cannot be tested ')

        self.is_eligible = False if self.error_message else True

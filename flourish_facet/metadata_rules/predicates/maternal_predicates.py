
from edc_constants.constants import POS
from edc_metadata_rules import PredicateCollection

from flourish_caregiver.helper_classes import MaternalStatusHelper


class MaternalPredicates(PredicateCollection):
    app_label = "flourish_facet"
    visit_model = f"{app_label}.facetvisit"

    def func_hiv_positive(self, visit=None, **kwargs):
        """
        Get HIV Status from the rapid test results
        """

        maternal_status_helper = MaternalStatusHelper(
            subject_identifier=visit.subject_identifier)

        return maternal_status_helper.hiv_status == POS

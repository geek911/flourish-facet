from edc_constants.constants import NO


class FacetEligibility:
    def __init__(self, facet_participation=None):
        self.error_message = []
        self.facet_participation = facet_participation

        if self.facet_participation == NO:
            self.error_message.append(
                'Not interested in participating in the Facet study'
            )
        self.is_eligible = False if self.error_message else True

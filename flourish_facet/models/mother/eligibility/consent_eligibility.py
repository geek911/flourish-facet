from edc_constants.constants import NO


class FacetConsentEligibility:
    def __init__(self, 
                 child_consent: str,
                 consent_reviewed: str,
                 assentment_score: str,
                 study_questions: str,
                 consent_signature: str,
                 consent_copy: str):
        
        self.error_message = []

        if child_consent == NO:
            self.error_message.append('Child cannot be consented')
        if consent_reviewed == NO:
            self.error_message.append('Consent not reviewed')

        if assentment_score == NO:
            self.error_message.append('Did not understand all the questions')

        if study_questions == NO:
            self.error_message.append('Did not answer all study question')

        if consent_signature == NO:
            self.error_message.append('Did not sign all the consent form')

        if consent_copy == NO:
            self.error_message.append('Declined copy')

        self.is_eligible = False if self.error_message else True

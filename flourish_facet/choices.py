from edc_constants.constants import OTHER, MALE, FEMALE, DONT_KNOW, ALIVE, DEAD, NEVER, PARTICIPANT, UNKNOWN
from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import YES, NO, NEG, POS, IND, FAILED_ELIGIBILITY, OFF_STUDY, ON_STUDY, NOT_APPLICABLE
from edc_visit_tracking.constants import COMPLETED_PROTOCOL_VISIT, MISSED_VISIT, \
    LOST_VISIT, SCHEDULED, UNSCHEDULED


REASONS_UNWILLING_FACET = (
    ('unable_to_provide_consent ', 'Mother unavailable to provide consent'),
    ('refuses_to_provide_consent', 'Mother refuses to provide consent'),
    ('unwilling_to_give_personal_info',
     'Unwilling to give Personal Info'),
    ('cannot_come_to_clinic', 'Cannot physically come to clinic'),
    ('not_interested', 'Not Interested in participating'),
    (OTHER, 'Other (Specify'),)

IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('country_id_rcpt', 'Country ID receipt'),
    ('passport', 'Passport'),
    (OTHER, 'Other'),
)

GENDER_OTHER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other')),
)

CHILD_IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('birth_cert', 'Birth Certificate number'),
    ('country_id_rcpt', 'Country ID receipt'),
    ('passport', 'Passport'),
    (OTHER, 'Other'),
)

CHILD_CONSENT_VERSION = (
    ('1', 'Consent version 1'),
    ('2', 'Consent version 2'),
    ('2.1', 'Consent version 2.1'),
    ('3', 'Consent version 3')
)

YES_NO_DNK = (
    (YES, YES),
    (NO, NO),
    (DONT_KNOW, 'Do not know')
)

POS_NEG_IND = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate')
)

AGE_BREASTFEEDING_ENDED = (
    ('older_than_6_weeks', 'Older than 6 weeks'),
    ('under_6_weeks', 'Under six weeks'),
    (DONT_KNOW, 'Do not know')

)

VISIT_REASON = [
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Missed Scheduled visit'),
    (UNSCHEDULED,
     'Unscheduled visit at which lab samples or data are being submitted'),
    (LOST_VISIT, 'Lost to follow-up (use only when taking subject off study)'),
    (FAILED_ELIGIBILITY, 'Subject failed enrollment eligibility'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study')
]

INFO_PROVIDER = (
    ('MOTHER', 'Mother'),
    ('GRANDMOTHER', 'Grandmother'),
    ('FATHER', 'Father'),
    ('GRANDFATHER', 'Grandfather'),
    ('SIBLING', 'Sibling'),
    ('self', 'Self'),
    (OTHER, 'Other'),
)

VISIT_STUDY_STATUS = (
    (ON_STUDY, 'On study'),
    (OFF_STUDY,
     'Off study-no further follow-up (including death); use only '
     'for last study contact'),
)
ALIVE_DEAD_UNKNOWN = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
    (UNKNOWN, 'Unknown'),
)

VISIT_INFO_SOURCE = [
    (PARTICIPANT, 'Clinic visit with participant'),
    ('other_contact',
     'Other contact with participant (for example telephone call)'),
    ('other_doctor',
     'Contact with external health care provider/medical doctor'),
    ('family',
     'Contact with family or designated person who can provide information'),
    ('chart', 'Hospital chart or other medical record'),
    (OTHER, 'Other')]

WEIGHT_RECORDED = [
    ('with_infant_scale', 'With infant scale'),
    ('with_adult_scale,', 'With adult scale,')
]

OCCURENCES = [
    ('never', 'Never'),
    ('rarely/sometimes', 'Rarely/Sometimes'),
    ('often', 'Often'),
]

MATERNAL_VISIT_STUDY_STATUS = (
    (ON_STUDY, 'On study'),
    (OFF_STUDY,
     'Off study-no further follow-up (including death); use only '
     'for last study contact'),
)

DRUG_COMBINATION = [
    ('TDF_+_3TC_+EFV', 'TDF + 3TC +EFV'),
    ('TDF_+_3TC_+_DTG', 'TDF + 3TC+ DTG'),
    ('AZT_+_3TC_+_EFV', 'AZT + 3TC +EFV'),
    ('AZT_+ 3TC_+_ATV/r', 'AZT + 3TC +ATV/r'),
    ('TDF_+_3TC_+_ATV/r', 'TDF + 3TC + ATV/r'),
    ('TDF_+_3TC_+_LPV/r', 'TDF + 3TC + LPV/r'),
    ('other_regimen_specify', 'Other regimen, specify')
]

REASONS_REGIMEN_CHANGE = [
    ('drug_resistance', 'Drug resistance'),
    ('side_effects', 'Side Effects'),
    ('recommendations_in_pregnancy', 'Recommendations in pregnancy'),
    (DONT_KNOW, 'Do not know'),
    ('other_specify', 'Other specify')
]

OCCURENCES_MORE = [
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('sometimes', 'Sometimes'),
    ('fairly_often', 'Fairly often'),
    ('frequently', 'Frequently'),
]

REASON_CHILD_NOT_TESTED = [
    (NOT_APPLICABLE, 'Not applicable'),
    ('mother_or_caregiver_have_not_yet_sought_to_clinic',
     'Mother or caregiver have not yet sought to clinic'),
    ('mother_or_caregiver_went_to_the_clinic_but_could_not_get_a_booking',
     'Mother or caregiver went to the clinic but could not get a booking'),
    ('health_worker_responsible_for_testing_not_available',
     'Health worker responsible for testing not available'),
    ('child’s_father_does_not_want_child_to_be_tested',
     'Child’s father does not want child to be tested'),
    ('family_other_than_child’s_father_does_not_want_child_to_be_tested',
     'Family other than child’s father does not want child to be tested'),
    ('mother_or_caregiver_work_constraints',
     'Mother or caregiver work constraints'),
    ('mother_or_caregiver_did_not_have_transport_fare_to_go_to_clinic_for_testing',
     'Mother or caregiver did not have transport fare to go to clinic for testing'),
    ('hiv_testing_kits_not_available', 'HIV Testing kits not available'),
    ('mother_or_caregiver_forgot_and_did_not_take_child_for_testing',
     'Mother or caregiver forgot and did not take child for testing'),
    ('diagnostic_machines_not_working', 'Diagnostic machines not working'),
    ('no_apparent_reason', 'No apparent reason'),
    ('other_specify', 'Other specify')
]

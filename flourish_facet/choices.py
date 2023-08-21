from edc_constants.constants import OTHER, MALE, FEMALE
from django.utils.translation import ugettext_lazy as _

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

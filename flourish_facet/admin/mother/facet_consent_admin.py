from django.contrib import admin
from ...models.mother import FacetConsent
from ...admin_site import flourish_facet_admin
from ...forms.mother import FacetConsentForm
from edc_model_admin import audit_fieldset_tuple


@admin.register(FacetConsent, site=flourish_facet_admin)
class FacetConsentAdmin(admin.ModelAdmin):

    form = FacetConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'consent_datetime',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'gender',
                'gender_other',
                'dob',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'consent_to_participate',
            )
        }), ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy',),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'language': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'identity_type': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'consent_to_participate': admin.VERTICAL
    }

    list_display = (
        'subject_identifier',
        'verified_by',
        'is_verified',
        'is_verified_datetime',
        'first_name',
        'initials',
        'gender',
        'dob',
        'consent_datetime',
        'created',
        'modified',
        'user_created',
        'user_modified',

    )
    search_fields = ('subject_identifier', 'dob')

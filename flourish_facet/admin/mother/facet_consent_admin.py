from django.contrib import admin
from ...models.mother import FacetConsent
from ...admin_site import flourish_facet_admin
from ...forms.mother import FacetConsentForm
from edc_model_admin import ModelAdminFormAutoNumberMixin, audit_fieldset_tuple
from edc_model_admin import StackedInlineMixin
from ...models import MotherChildConsent
from ...forms import MotherChildConsentForm
from simple_history.admin import SimpleHistoryAdmin
from edc_model_admin import ModelAdminBasicMixin


class MotherChildConsentInline(StackedInlineMixin, ModelAdminFormAutoNumberMixin,
                               admin.StackedInline):
    model = MotherChildConsent
    form = MotherChildConsentForm

    extra = 0
    max_num = 1

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'first_name',
                'last_name',
                'gender',
                'child_dob',
                'child_test',
                'identity',
                'identity_type',
                'confirm_identity',
                'consent_datetime'
            ]}
         ),)

    radio_fields = {'gender': admin.VERTICAL,
                    'child_test': admin.VERTICAL,
                    'identity_type': admin.VERTICAL, }

    def save_model(self, request, obj, form, change):
        super(MotherChildConsentInline, self).save_model(
            request, obj, form, change)


@admin.register(FacetConsent, site=flourish_facet_admin)
class FacetConsentAdmin(ModelAdminBasicMixin, SimpleHistoryAdmin,
                        admin.ModelAdmin):

    form = FacetConsentForm
    inlines = [MotherChildConsentInline, ]

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
                'child_consent',
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
        'consent_to_participate': admin.VERTICAL,
        'assessment_score': admin.VERTICAL,
        'consent_copy': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'study_questions': admin.VERTICAL,
        'child_consent': admin.VERTICAL

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


@admin.register(MotherChildConsent, site=flourish_facet_admin)
class MotherChildConsentAdmin(admin.ModelAdmin):
    form = MotherChildConsentForm

    fieldsets = (
        (None, {
            'fields': [
                'facet_consent',
                'subject_identifier',
                'first_name',
                'last_name',
                'gender',
                'child_dob',
                'child_test',
                'identity',
                'identity_type',
                'confirm_identity',
                'version',
                'consent_datetime'
            ]
        }), audit_fieldset_tuple
    )

    radio_fields = {'gender': admin.VERTICAL,
                    'child_test': admin.VERTICAL,
                    'identity_type': admin.VERTICAL}

    list_display = ('subject_identifier',
                    'verified_by',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'last_name',
                    'gender',
                    'child_dob',
                    'consent_datetime',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')

    list_filter = ('is_verified',
                   'gender',
                   'identity_type')

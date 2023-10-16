from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.apps import apps as django_apps
from dateutil.relativedelta import relativedelta
from edc_model_admin import StackedInlineMixin
from functools import partialmethod
from edc_base.utils import get_utcnow
from ...models.mother import FacetConsent
from ...admin_site import flourish_facet_admin
from ...forms.mother import FacetConsentForm
from edc_model_admin import ModelAdminFormAutoNumberMixin, audit_fieldset_tuple
from edc_model_admin import StackedInlineMixin
from ...models import MotherChildConsent
from ...forms import MotherChildConsentForm
from simple_history.admin import SimpleHistoryAdmin
from ..modeladmin_mixins import ModelAdminMixin


class MotherChildConsentInline(StackedInlineMixin, ModelAdminFormAutoNumberMixin,
                               admin.StackedInline):
    model = MotherChildConsent
    form = MotherChildConsentForm
    caregiver_child_consent_model = 'flourish_caregiver.caregiverchildconsent'
    antenatal_enrollment_model = 'flourish_caregiver.antenatalenrollment'

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

    @property
    def caregiver_child_consent_cls(self):
        return django_apps.get_model(self.caregiver_child_consent_model)

    @property
    def antenatal_enrollment_cls(self):
        return django_apps.get_model(self.antenatal_enrollment_model)

    def get_formset(self, request, obj, **kwargs):
        initial = []

        subject_identifier = request.GET.get('subject_identifier', None)

        if subject_identifier:

            anc_subject_identifiers = self.antenatal_enrollment_cls.objects.values_list(
                'subject_identifier')

            children = self.caregiver_child_consent_cls.objects.filter(
                first_name__isnull=False,
                last_name__isnull=False,
                subject_consent__subject_identifier=subject_identifier,
                subject_consent__subject_identifier__in=anc_subject_identifiers)

            for child in children:
                age = relativedelta(get_utcnow().date(),
                                    child.child_dob)

                if age.years == 0 and age.months <= 6:
                    initial.append({
                        'first_name': child.first_name,
                        'last_name': child.last_name,
                        'gender': child.gender,
                        'child_dob': child.child_dob,
                        'subject_identifier': child.subject_identifier})

            self.extra = len(initial)

        formset = super().get_formset(request, obj, **kwargs)
        formset.__init__ = partialmethod(formset.__init__, initial=initial)

        return formset

    def save_model(self, request, obj, form, change):
        super(MotherChildConsentInline, self).save_model(
            request, obj, form, change)


@admin.register(FacetConsent, site=flourish_facet_admin)
class FacetConsentAdmin(ModelAdminMixin, SimpleHistoryAdmin,
                        admin.ModelAdmin):

    form = FacetConsentForm
    inlines = [MotherChildConsentInline, ]

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
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
                'consent_datetime',

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
                'consent_datetime'
            ]
        }), audit_fieldset_tuple
    )

    radio_fields = {'gender': admin.VERTICAL,
                    'child_test': admin.VERTICAL,
                    'identity_type': admin.VERTICAL}

    list_display = ('subject_identifier',
                    'first_name',
                    'last_name',
                    'gender',
                    'child_dob',
                    'consent_datetime',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')

    list_filter = (
        'gender',
        'identity_type')

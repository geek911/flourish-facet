from edc_base.utils import get_utcnow, get_uuid
from django.apps import apps as django_apps
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import MALE
from edc_dashboard.views import DashboardView as BaseDashboardView
from edc_navbar import NavbarViewMixin
from edc_subject_dashboard.view_mixins import SubjectDashboardViewMixin
from ...model_wrappers import (
    MotherAppointmentModelWrapper, MotherVisitModelWrapper,
    FacetConsentModelWrapper, LocatorModelWrapper, FacetMotherCrfModelWrapper)


class FacetMotherDashboardView(EdcBaseViewMixin, SubjectDashboardViewMixin,
                               NavbarViewMixin, BaseDashboardView):
    dashboard_url = 'facet_mother_dashboard_url'
    dashboard_template = 'facet_mother_dashboard_template'
    appointment_model_wrapper_cls = MotherAppointmentModelWrapper
    consent_model = 'flourish_facet.facetconsent'
    consent_model_wrapper_cls = FacetConsentModelWrapper
    subject_locator_model = 'flourish_caregiver.caregiverlocator'
    subject_locator_model_wrapper_cls = LocatorModelWrapper
    visit_model_wrapper_cls = MotherVisitModelWrapper
    crf_model_wrapper_cls = FacetMotherCrfModelWrapper
    navbar_name = 'flourish_facet'
    visit_attr = 'facetvisit'
    infant_links = True
    mother_infant_study = True
    maternal_links = False
    infant_dashboard_include_value = 'flourish_facet/mother/dashboard/dashboard_links.html'
    infant_subject_dashboard_url = 'facet_child_dashboard_url'

    child_consent_model = 'flourish_facet.motherchildconsent'

    @property
    def consent_cls(self):
        return django_apps.get_model(self.consent_model)

    @property
    def child_consent_cls(self):
        return django_apps.get_model(self.child_consent_model)

    @property
    def consent_object(self):
        """Returns a consent_config object or None
        from site_consents for the current reporting period.
        """
        try:
            consent_object = self.consents.filter(
                subject_identifier=self.subject_identifier
            ).latest('consent_datetime')
        except self.consent_cls.DoesNotExist:
            consent_object = None
        return consent_object

    @property
    def consent(self):
        """Returns a consent model instance or None for the current period.
        """
        return self.consent_object

    @property
    def consent_wrapped(self):
        """Returns a wrapped consent, either saved or not,
        for the current period.
        """
        return self.consent_model_wrapper_cls(self.consent or self.empty_consent)

    @property
    def empty_consent(self):
        """Returns an unsaved consent model instance.

        Override to include additional attrs to instantiate.
        """
        return self.consent_object.model_cls(
            subject_identifier=self.subject_identifier,
            consent_identifier=get_uuid(),
            version=self.consent_object.version)

    @property
    def consents(self):
        """Returns a Queryset of consents for this subject.
        """
        return self.consent_cls.objects.filter(
            subject_identifier=self.subject_identifier)

    @property
    def consents_wrapped(self):
        """Returns a generator of wrapped consents.
        """
        return (self.consent_model_wrapper_cls(obj) for obj in self.consents)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visit_schedules = {'f_mother_visit_schedule': self.visit_schedules.get(
            'f_mother_visit_schedule')}
        context.update(
            visit_schedules=visit_schedules,
            mother_infant_study=self.mother_infant_study
        )
        return context

    def set_current_schedule(self, onschedule_model_obj=None,
                             schedule=None, visit_schedule=None,
                             is_onschedule=True):
        # int()
        if onschedule_model_obj and is_onschedule:
            self.current_schedule = schedule
            self.current_visit_schedule = visit_schedule
            self.current_onschedule_model = onschedule_model_obj
        self.onschedule_models.append(onschedule_model_obj)
        self.visit_schedules.update(
            {visit_schedule.name: visit_schedule})

    def get_onschedule_model_obj(self, schedule):
        try:
            return schedule.onschedule_model_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except ObjectDoesNotExist:
            return None

    @property
    def mother_infant_study(self):
        return self.child_consent_cls.objects.filter(facet_consent=self.consent_object).first()

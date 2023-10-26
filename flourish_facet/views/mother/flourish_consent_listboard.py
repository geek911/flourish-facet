
from django.apps import apps as django_apps
from django.db.models import Q
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from flourish_facet.views.eligible_facet_participants_mixin import EligibleFacetParticipantsMixin
from ...model_wrappers import FlourishConsentModelWrapper


class FlourishConsentListboardView(EdcBaseViewMixin, NavbarViewMixin, SearchFormViewMixin,
                                   ListboardView, EligibleFacetParticipantsMixin):

    listboard_template = 'facet_flourish_consent_template'
    listboard_url = 'facet_flourish_consent_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"
    search_form_url = 'facet_flourish_consent_listboard_url'

    model = 'flourish_caregiver.subjectconsent'
    model_wrapper_cls = FlourishConsentModelWrapper
    navbar_name = 'flourish_facet'
    navbar_selected_item = 'flourish_consent_listboard'

    flourish_child_consent_model = 'flourish_caregiver.caregiverchildconsent'
    child_hiv_rapid_test_model = 'flourish_child.childhivrapidtestcounseling'
    antenatal_enrollment_model = 'flourish_caregiver.antenatalenrollment'
    facet_screening_model = 'flourish_facet.facetsubjectscreening'

    @property
    def antenatal_enrollment_cls(self):
        return django_apps.get_model(self.antenatal_enrollment_model)

    @property
    def flourish_child_consent_cls(self):
        return django_apps.get_model(self.flourish_child_consent_model)

    @property
    def facet_screening_cls(self):
        return django_apps.get_model(self.facet_screening_model)

    @property
    def child_hiv_rapid_test_cls(self):
        return django_apps.get_model(self.child_hiv_rapid_test_model)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return self.eligible_participants(queryset)

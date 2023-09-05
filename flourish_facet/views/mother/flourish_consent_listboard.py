import re
from edc_base.utils import get_utcnow
from dateutil.relativedelta import relativedelta
from django.db.models import ExpressionWrapper
from django.apps import apps as django_apps
from django.db.models import Q
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from edc_constants.constants import YES
from ...model_wrappers import FlourishConsentModelWrapper


class FlourishConsentListboardView(EdcBaseViewMixin, NavbarViewMixin,
                                   ListboardView):

    listboard_template = 'facet_flourish_consent_template'
    listboard_url = 'facet_flourish_consent_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"

    model = 'flourish_caregiver.subjectconsent'
    model_wrapper_cls = FlourishConsentModelWrapper
    navbar_name = 'flourish_facet'
    navbar_selected_item = 'flourish_consent_listboard'
    flourish_child_consent_model = 'flourish_caregiver.caregiverchildconsent'
    child_hiv_rapid_test_model = 'flourish_child.childhivrapidtestcounseling'

    @property
    def flourish_child_consent_cls(self):
        return django_apps.get_model(self.flourish_child_consent_model)
    
    @property
    def child_hiv_rapid_test_cls(self):
        return django_apps.get_model(self.child_hiv_rapid_test_model)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        return options

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        dates_before = (get_utcnow() - relativedelta(months=6)).date().isoformat()

        today = get_utcnow().date().isoformat()

        subject_identifiers = self.flourish_child_consent_cls.objects.filter(
            child_dob__range=[dates_before, today],
        ).values_list('subject_consent__subject_identifier', flat=True)

        return queryset.filter(subject_identifier__in=subject_identifiers, 
                               future_contact=YES)

import re

from django.apps import apps as django_apps
from django.db.models import Q
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ...model_wrappers import FacetConsentModelWrapper


class FacetMotherConsentListboardView(EdcBaseViewMixin,
                                      NavbarViewMixin,
                                      ListboardFilterViewMixin,
                                      SearchFormViewMixin,
                                      ListboardView):

    listboard_template = 'facet_mother_listboard_template'
    listboard_url = 'facet_mother_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"

    model = 'flourish_facet.facetconsent'
    model_wrapper_cls = FacetConsentModelWrapper
    navbar_name = 'flourish_facet'
    navbar_selected_item = 'facet_mother_listboard'

    search_form_url = 'subject_listboard_url'

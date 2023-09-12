import re

from django.apps import apps as django_apps
from django.db.models import Q
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ...model_wrappers import FacetChildConsentModelWrapper


class FacetChildConsentListboardView(EdcBaseViewMixin, NavbarViewMixin,
                                     ListboardView):

    listboard_template = 'facet_child_listboard_template'
    listboard_url = 'facet_child_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"

    model = 'flourish_facet.motherchildconsent'
    model_wrapper_cls = FacetChildConsentModelWrapper
    navbar_name = 'flourish_facet'
    navbar_selected_item = 'facet_child_listboard'

import re
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView as BaseListboardView

from ...model_wrappers import FocusGroupInterviewAudioUploadModelWrapper


class GroupInterviewListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                                  ListboardFilterViewMixin, SearchFormViewMixin, BaseListboardView):

    listboard_template = 'group_interview_listboard_template'
    listboard_url = 'group_interview_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"
    model = 'flourish_facet.focusgroupinterviewaudiouploads'
    model_wrapper_cls = FocusGroupInterviewAudioUploadModelWrapper
    navbar_name = 'flourish_facet'
    navbar_selected_item = 'group_interview_listboard'
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'group_interview_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            focus_group_audio_upload_add_url=self.model_cls().get_absolute_url())
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('group_identifier'):
            options.update(
                {'group_identifier': kwargs.get('group_identifier')}, )
        return options

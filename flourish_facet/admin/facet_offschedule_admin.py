from django.contrib import admin
from ..models import FacetMotherOffSchedule, FacetChildOffSchedule
from ..admin_site import flourish_facet_admin
from .modeladmin_mixins import ModelAdminMixin
from django.conf import settings
from django.urls import reverse_lazy
from edc_model_admin import audit_fieldset_tuple


@admin.register(FacetMotherOffSchedule, site=flourish_facet_admin)
class FacetMotherOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):
    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'offstudy_date',
                'reason',
                'reason_other',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {'reason': admin.VERTICAL}

    def redirect_url(self, request, obj, post_url_continue=None):

        subject_identifier = obj.subject_identifier

        if len(subject_identifier) > 16:
            url = 'facet_child_dashboard_url'
        else:
            url = 'facet_mother_dashboard_url'

        return reverse_lazy(
            settings.DASHBOARD_URL_NAMES.get(url), args=(subject_identifier,))


@admin.register(FacetChildOffSchedule, site=flourish_facet_admin)
class FacetChildOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):
    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'offstudy_date',
                'reason',
                'reason_other',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {'reason': admin.VERTICAL}

    def redirect_url(self, request, obj, post_url_continue=None):

        subject_identifier = obj.subject_identifier

        if len(subject_identifier) > 16:
            url = 'facet_child_dashboard_url'
        else:
            url = 'facet_mother_dashboard_url'

        return reverse_lazy(
            settings.DASHBOARD_URL_NAMES.get(url), args=(subject_identifier,))

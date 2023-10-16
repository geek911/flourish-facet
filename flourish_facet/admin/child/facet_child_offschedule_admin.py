from flourish_facet.admin.modeladmin_mixins import ModelAdminMixin
from flourish_facet.admin_site import flourish_facet_admin
from flourish_facet.models import FacetChildOffSchedule


from django.conf import settings
from django.contrib import admin
from django.urls import reverse_lazy
from edc_model_admin import audit_fieldset_tuple


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

        url = 'facet_child_dashboard_url'
        return reverse_lazy(
            settings.DASHBOARD_URL_NAMES.get(url), args=(subject_identifier,))

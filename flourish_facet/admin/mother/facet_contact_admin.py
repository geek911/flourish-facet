from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...models import FacetContact
from ...forms import FacetContactForm
from ...admin.modeladmin_mixins import ModelAdminMixin
from ...admin_site import flourish_facet_admin


@admin.register(FacetContact, site=flourish_facet_admin)
class FacetContactAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = FacetContactForm

    search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'contact_type',
                'contact_datetime',
                'call_reason',
                'call_reason_other',
                'contact_success',
                'contact_comment',
                'call_rescheduled',
                'reason_rescheduled',
                'reason_rescheduled_other',
            )}
         ), audit_fieldset_tuple)

    list_display = [
        'subject_identifier', 'contact_type',
        'contact_datetime', 'call_reason', 'contact_success']

    list_filter = ['contact_type', 'call_reason', 'contact_success']

    radio_fields = {
        'contact_type': admin.VERTICAL,
        'call_reason': admin.VERTICAL,
        'contact_success': admin.VERTICAL,
        'call_rescheduled': admin.VERTICAL,
        'reason_rescheduled': admin.VERTICAL,
    }

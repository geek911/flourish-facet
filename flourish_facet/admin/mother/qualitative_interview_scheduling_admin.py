from django.contrib import admin
from ...models import QualitativeInterviewScheduling
from ...admin_site import flourish_facet_admin
from ...forms import QualitativeInterviewSchedulingForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import ModelAdminMixin


@admin.register(QualitativeInterviewScheduling, site=flourish_facet_admin)
class QualitativeInterviewSchedulingAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = QualitativeInterviewSchedulingForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'qualitative_type',
                'google_sheet_calendar',
                'facet_consent_form',
                'complete',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'qualitative_type': admin.VERTICAL,
        'google_sheet_calendar': admin.VERTICAL,
        'facet_consent_form': admin.VERTICAL,
        'complete': admin.VERTICAL,
    }

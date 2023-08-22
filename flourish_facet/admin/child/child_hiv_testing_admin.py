from django.contrib import admin
from ...models import ChildHivTesting
from ...admin_site import flourish_facet_admin
from ...forms import ChildHivTestingForm
from edc_model_admin import audit_fieldset_tuple
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ChildHivTesting, site=flourish_facet_admin)
class ChildHivTestingAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = ChildHivTestingForm

    fieldsets = (
        (None, {
            'fields': [
                'child_tested',
                'reason_not_tested',
                'child_tested_6_weeks',
                'hiv_result_6_weeks',
                'reason_not_tested_6_weeks',
                'child_breastfed',
                'child_breastfeeding',
                'child_breastfed_tested',
                'child_breastfed_tested_result',
                'reason_not_tested_3_months',
                'child_breastfed_end'
            ]}), audit_fieldset_tuple
    )

    radio_fields = {
        'child_tested': admin.VERTICAL,
        'child_tested_6_weeks': admin.VERTICAL,
        'hiv_result_6_weeks': admin.VERTICAL,
        'child_breastfed': admin.VERTICAL,
        'child_breastfeeding': admin.VERTICAL,
        'child_breastfed_tested': admin.VERTICAL,
        'child_breastfed_tested_result': admin.VERTICAL,
        'child_breastfed_end': admin.VERTICAL,
    }

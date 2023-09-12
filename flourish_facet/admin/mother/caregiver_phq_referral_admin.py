from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import flourish_facet_admin
from ...forms import FacetCaregiverPhqReferralForm
from ...models import FacetCaregiverPhqReferral
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(FacetCaregiverPhqReferral, site=flourish_facet_admin)
class FacetCaregiverPhqReferralAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = FacetCaregiverPhqReferralForm

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
                'report_datetime',
                'referred_to',
                'referred_to_other',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {'referred_to': admin.VERTICAL}

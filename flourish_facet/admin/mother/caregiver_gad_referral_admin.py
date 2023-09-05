from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import flourish_facet_admin
from ...forms import FacetCaregiverGadReferralForm
from ...models import FacetCaregiverGadReferral
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(FacetCaregiverGadReferral, site=flourish_facet_admin)
class FacetCaregiverGadReferralAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = FacetCaregiverGadReferralForm

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

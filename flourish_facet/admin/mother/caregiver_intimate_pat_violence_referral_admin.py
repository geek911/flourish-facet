from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import flourish_facet_admin
from ...forms import IntimatePartnerViolenceReferralForm
from ...models import IntimatePartnerViolenceReferral
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(IntimatePartnerViolenceReferral, site=flourish_facet_admin)
class IntimatePartnerViolenceReferralAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = IntimatePartnerViolenceReferralForm

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

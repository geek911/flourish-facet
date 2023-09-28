from django.contrib import admin
from ...admin_site import flourish_facet_admin
from ...models import IntimatePartnerViolence
from ...forms import IntimatePartnerViolenceForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(IntimatePartnerViolence, site=flourish_facet_admin)
class IntimatePartnerViolenceAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = IntimatePartnerViolenceForm
    fieldsets = (
        (None, {
            'fields': (
                'facet_visit',
                'report_datetime',
                'physically_hurt',
                'insult_talk',
                'threaten',
                'scream_curse',
            )
        }), audit_fieldset_tuple
    )

    radio_fields = {
        'physically_hurt': admin.VERTICAL,
        'insult_talk': admin.VERTICAL,
        'threaten': admin.VERTICAL,
        'scream_curse': admin.VERTICAL,
    }

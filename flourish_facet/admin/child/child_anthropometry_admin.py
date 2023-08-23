from django.contrib import admin
from ...admin_site import flourish_facet_admin
from ...forms import ChildAnthropometryForm
from ...models import ChildAnthropometry
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(ChildAnthropometry, site=flourish_facet_admin)
class ChildAnthropomentryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = ChildAnthropometryForm

    fieldsets = (
        (None, {
            'fields': (
                'facet_visit',
                'report_datetime',
                'has_oedema',
                'weight_1',
                'weight_2',
                'weight_3',
                'weight_recorded',
                'length_1',
                'length_2',
                'length_3',
            )
        }), audit_fieldset_tuple
    )

    radio_fields = {
        'has_oedema': admin.HORIZONTAL,
        'weight_recorded': admin.VERTICAL,
    }

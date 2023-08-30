from django.contrib import admin
from ...models import HouseholdHungerScale
from ...forms import HouseholdHungerScaleForm
from edc_model_admin import audit_fieldset_tuple
from ...admin_site import flourish_facet_admin
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(HouseholdHungerScale, site=flourish_facet_admin)
class HouseholdHungerScaleAdmin(admin.ModelAdmin):
    form = HouseholdHungerScaleForm

    fieldsets = (
        (None, {
            'fields': (
                'facet_visit',
                'report_datetime',
                'no_food',
                'no_food_night',
                'no_food_day_night',
            )
        }), audit_fieldset_tuple
    )

    radio_fields = {
        'no_food': admin.HORIZONTAL,
        'no_food_night': admin.HORIZONTAL,
        'no_food_day_night': admin.HORIZONTAL
    }

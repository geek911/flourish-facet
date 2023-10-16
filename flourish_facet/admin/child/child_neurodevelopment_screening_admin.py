from django.contrib import admin
from ...admin_site import flourish_facet_admin
from ...models import ChildNeurodevelopmentScreening
from ...forms import ChildNeurodevelopmentScreeningForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(ChildNeurodevelopmentScreening, site=flourish_facet_admin)
class ChildNeurodevelopmentScreeningAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = ChildNeurodevelopmentScreeningForm

    fieldsets = (
        (None, {
            'fields': (
                'facet_visit',
                'report_datetime',
                'can_move_eyes',
                'can_respond_sound',
                'can_eyes_move',
                'can_recognize',
                'can_laugh',
                'can_use_sounds',
                'can_grasp',
                'can_lift',

            )
        }), audit_fieldset_tuple
    )
    radio_fields = {
        'can_move_eyes': admin.VERTICAL,
        'can_respond_sound': admin.VERTICAL,
        'can_eyes_move': admin.VERTICAL,
        'can_recognize': admin.VERTICAL,
        'can_laugh': admin.VERTICAL,
        'can_use_sounds': admin.VERTICAL,
        'can_grasp': admin.VERTICAL,
        'can_lift': admin.VERTICAL,
    }

from django.contrib import admin
from edc_fieldsets.fieldlist import Insert
from edc_fieldsets.fieldsets_modeladmin_mixin import FormLabel
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import flourish_facet_admin
from ...forms import ChildSocioDemographicForm
from ...models import FacetChildSocioDemographic
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(FacetChildSocioDemographic, site=flourish_facet_admin)
class ChildSocioDemographicAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = ChildSocioDemographicForm

    list_display = ('facet_visit',
                    'ethnicity')
    list_filter = ('ethnicity',)

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
                'report_datetime',
                'ethnicity',
                'ethnicity_other',
                'stay_with_caregiver',
                'water_source',
                'house_electrified',
                'house_fridge',
                'cooking_method',
                'toilet_facility',
                'toilet_facility_other',
                'house_people_number',
                'older_than18',
                'house_type',
                'attend_school',
                'education_level',
                'education_level_other',
                'school_type',
                'working']}
         ), audit_fieldset_tuple)

    radio_fields = {'ethnicity': admin.VERTICAL,
                    'stay_with_caregiver': admin.VERTICAL,
                    'water_source': admin.VERTICAL,
                    'house_electrified': admin.VERTICAL,
                    'house_fridge': admin.VERTICAL,
                    'cooking_method': admin.VERTICAL,
                    'toilet_facility': admin.VERTICAL,
                    'house_type': admin.VERTICAL,
                    'attend_school': admin.VERTICAL,
                    'education_level': admin.VERTICAL,
                    'school_type': admin.VERTICAL,
                    'working': admin.VERTICAL,
                    'socio_demo_changed': admin.VERTICAL}

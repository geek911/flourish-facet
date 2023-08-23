from django.contrib import admin
from ...models.mother import FacetSubjectScreening
from ...admin_site import flourish_facet_admin
from ...forms.mother import FacetSubjectScreeningForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import ModelAdminMixin


@admin.register(FacetSubjectScreening, site=flourish_facet_admin)
class FacetSubjectScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = FacetSubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'facet_participation',
                'reasons_unwilling_part',
                'reasons_unwilling_part_other',

            ]
        }), audit_fieldset_tuple
    )

    radio_fields = {
        'facet_participation': admin.VERTICAL,
        'reasons_unwilling_part': admin.VERTICAL,
    }

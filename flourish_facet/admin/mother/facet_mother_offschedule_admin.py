from django.contrib import admin
from ...models import FacetMotherOffSchedule
from ...forms import FacetVisitForm
from ...admin_site import flourish_facet_admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin


@admin.register(FacetMotherOffSchedule, site=flourish_facet_admin)
class FacetMotherOffScheduleAdmin(admin.ModelAdmin):
    pass

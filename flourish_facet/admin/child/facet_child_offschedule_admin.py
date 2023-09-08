from django.contrib import admin
from ...models import FacetChildOffSchedule
from ...admin_site import flourish_facet_admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin


@admin.register(FacetChildOffSchedule, site=flourish_facet_admin)
class FacetChildOffScheduleAdmin(admin.ModelAdmin):
    pass
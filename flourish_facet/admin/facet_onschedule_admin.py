from django.contrib import admin
from ..models import OnScheduleFacetChild, OnScheduleFacetMother
from ..forms import FacetVisitForm
from ..admin_site import flourish_facet_admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin
from .modeladmin_mixins import ModelAdminMixin

@admin.register(OnScheduleFacetMother, site=flourish_facet_admin)
class OnScheduleFacetMotherAdmin(admin.ModelAdmin):
    pass

@admin.register(OnScheduleFacetChild, site=flourish_facet_admin)
class OnScheduleFacetChildAdmin(admin.ModelAdmin):
    pass
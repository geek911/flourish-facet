from django.contrib import admin
from ..models import Appointment
from ..forms import FacetAppointmentForm
from ..admin_site import flourish_facet_admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_appointment.admin import AppointmentAdmin as BaseAppointmentAdmin

@admin.register(Appointment, site=flourish_facet_admin)
class FacetAppointmentAdmin(BaseAppointmentAdmin):

    form = FacetAppointmentForm
from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_odk.admin import ODKActionMixin

from ..admin_site import flourish_facet_admin
from ..forms import FacetClinicianNotesForm, FacetClinicianNotesImageForm
from ..models import FacetClinicianNotesImage, FacetClinicianNotes
from .modeladmin_mixins import CrfModelAdminMixin
  

class ClinicianNotesImageInline(TabularInlineMixin, admin.TabularInline):

    model = FacetClinicianNotesImage
    form = FacetClinicianNotesImageForm
    extra = 0

    fields = ('clinician_notes_image', 'image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = ('clinician_notes_image', 'datetime_captured',
                  'user_uploaded') + fields

        return fields


@admin.register(FacetClinicianNotes, site=flourish_facet_admin)
class ClinicianNotesAdmin(ODKActionMixin, CrfModelAdminMixin,
                          admin.ModelAdmin):

    form = FacetClinicianNotesForm

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
            ]}
         ), )

    list_display = ('facet_visit', 'created', 'verified_by', 'is_verified',)

    inlines = [ClinicianNotesImageInline]

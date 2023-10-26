from django.contrib import admin
from flourish_facet.models.mother.facet_consent import FacetConsent
from ...models import FocusGroupInterviewAudioUploads
from ...admin_site import flourish_facet_admin
from ...forms import FocusGroupInterviewAudioUploadsForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import ModelAdminMixin
from edc_list_data import PreloadData


@admin.register(FocusGroupInterviewAudioUploads, site=flourish_facet_admin)
class FocusGroupInterviewAudioUploadsAdmin(ModelAdminMixin, admin.ModelAdmin):
    readonly_fields = ('group_identifier',)
    form = FocusGroupInterviewAudioUploadsForm

    fieldsets = (
        (None, {
            'fields': [
                'group_identifier',
                'paticipant_ids',
                'report_datetime',
                'location',
                'location_other',
                'interview_duration',
                'interview_language',
                'audio_file',
                'notes',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'location': admin.VERTICAL,
        'interview_language': admin.VERTICAL,
    }

    filter_horizontal = ['paticipant_ids',]

    def add_view(self, request, form_url='', extra_context=None):
        self.load_list_data()
        return super().add_view(request, form_url, extra_context)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'paticipant_ids':
            kwargs['queryset'] = self.get_subject_identifiers
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    @property
    def get_subject_identifiers(self):
        subject_identifiers = FacetConsent.objects.exclude(
            subject_identifier__in=self.get_used_identifiers).values_list(
            'subject_identifier', flat=True)
        return subject_identifiers

    @property
    def get_used_identifiers(self):
        return FocusGroupInterviewAudioUploads.objects.values_list(
            'paticipant_ids__name', flat=True)

    def load_list_data(self):
        subject_identifiers = list(set(self.get_subject_identifiers))
        subject_id_list = [(identifier, identifier)
                           for identifier in subject_identifiers]

        list_data = {'flourish_facet.fgfsubjectidentifiers': subject_id_list}
        PreloadData(list_data=list_data)

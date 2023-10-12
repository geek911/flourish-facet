from django.contrib import admin
from ...models import QualitativeInterviewAudioUploads
from ...admin_site import flourish_facet_admin
from ...forms import QualitativeInterviewAudioUploadsForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import ModelAdminMixin


@admin.register(QualitativeInterviewAudioUploads, site=flourish_facet_admin)
class QualitativeInterviewAudioUploadsAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = QualitativeInterviewAudioUploadsForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
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

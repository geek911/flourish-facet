from django.contrib import admin
from ...models import QualitativeInterviewTranscriptionAndTranslation
from ...admin_site import flourish_facet_admin
from ...forms import QualitativeInterviewTranscriptionAndTranslationForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import ModelAdminMixin


@admin.register(QualitativeInterviewTranscriptionAndTranslation, site=flourish_facet_admin)
class QualitativeInterviewTranscriptionAndTranslationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = QualitativeInterviewTranscriptionAndTranslationForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'transcription_date',
                'transcription_upload',
                'facet_member_transcription',
                'transcription_duration',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'facet_member_transcription': admin.VERTICAL,
        'transcription_duration': admin.VERTICAL,
    }

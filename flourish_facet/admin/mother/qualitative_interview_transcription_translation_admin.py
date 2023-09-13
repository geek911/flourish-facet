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
                'transcription_date',
                'transcription_upload',
                'facet_member_transcription',
                'transcription_duration',
                'translation_date',
                'translation_upload',
                'facet_member_translation',
                'complete',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'transcription_upload': admin.VERTICAL,
        'facet_member_transcription': admin.VERTICAL,
        'transcription_duration': admin.VERTICAL,
        'translation_upload': admin.VERTICAL,
        'facet_member_translation': admin.VERTICAL,
        'complete': admin.VERTICAL,
    }

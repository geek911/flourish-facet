from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..modeladmin_mixins import CrfModelAdminMixin
from ...admin_site import flourish_facet_admin
from ...forms import AnxietyScreeningGad7Form
from ...models import AnxietyScreeningGad7


@admin.register(AnxietyScreeningGad7, site=flourish_facet_admin)
class AnxietyScreeningGad7Admin(CrfModelAdminMixin, admin.ModelAdmin):

    form = AnxietyScreeningGad7Form

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
                'report_datetime',
                'feeling_anxious',
                'control_worrying',
                'worrying',
                'trouble_relaxing',
                'restlessness',
                'easily_annoyed',
                'fearful',
                'anxiety_score'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {'feeling_anxious': admin.VERTICAL,
                    'control_worrying': admin.VERTICAL,
                    'worrying': admin.VERTICAL,
                    'trouble_relaxing': admin.VERTICAL,
                    'restlessness': admin.VERTICAL,
                    'easily_annoyed': admin.VERTICAL,
                    'fearful': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        return ('anxiety_score', ) + fields

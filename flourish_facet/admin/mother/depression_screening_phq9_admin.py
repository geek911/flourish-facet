from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..modeladmin_mixins import CrfModelAdminMixin
from ...admin_site import flourish_facet_admin
from ...forms import DepressionScreeningPhq9Form
from ...models import DepressionScreeningPhq9


@admin.register(DepressionScreeningPhq9, site=flourish_facet_admin)
class DepressionScreeningPhq9Admin(CrfModelAdminMixin, admin.ModelAdmin):
    form = DepressionScreeningPhq9Form

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
                'report_datetime',
                'activity_interest',
                'depressed',
                'sleep_disorders',
                'fatigued',
                'eating_disorders',
                'self_doubt',
                'easily_distracted',
                'restlessness',
                'self_harm',
                'depression_score'
            ]}
         ), audit_fieldset_tuple)

    additional_instructions = (
        'Over the last 2 weeks, how often have you been bothered by any '
        'of the following problems?'
    )

    radio_fields = {'activity_interest': admin.VERTICAL,
                    'depressed': admin.VERTICAL,
                    'sleep_disorders': admin.VERTICAL,
                    'fatigued': admin.VERTICAL,
                    'eating_disorders': admin.VERTICAL,
                    'self_doubt': admin.VERTICAL,
                    'easily_distracted': admin.VERTICAL,
                    'restlessness': admin.VERTICAL,
                    'self_harm': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        return ('depression_score',) + fields

    additional_instructions = "Over the last 2 weeks, How often have you been bothered by the following problems?"

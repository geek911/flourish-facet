from functools import partialmethod
from django.apps import apps as django_apps
from django.contrib import admin
from edc_fieldsets.fieldlist import Fieldlist
from edc_fieldsets.fieldsets_modeladmin_mixin import FormLabel
from edc_model_admin import StackedInlineMixin, ModelAdminFormAutoNumberMixin, audit_fieldset_tuple

from ...admin_site import flourish_facet_admin
from ...forms import FacetSocioDemographicDataForm
from ...models import FacetSocioDemographicData, FacetConsent, FacetVisit
from ..modeladmin_mixins import CrfModelAdminMixin
from edc_fieldsets import Fieldsets


@admin.register(FacetSocioDemographicData, site=flourish_facet_admin)
class SocioDemographicDataAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = FacetSocioDemographicDataForm

    list_display = ('facet_visit',
                    'marital_status',
                    'ethnicity',
                    'highest_education')
    list_filter = ('marital_status',
                   'ethnicity',
                   'highest_education')

    fieldsets = (
        (None, {
            'fields': [
                'facet_visit',
                'report_datetime',
                'marital_status',
                'marital_status_other',
                'ethnicity',
                'ethnicity_other',
                'highest_education',
                'current_occupation',
                'current_occupation_other',
                'provides_money',
                'provides_money_other',
                'money_earned',
                'money_earned_other',
                'contributes_to_expenses',
                'expense_contributors',
                'expense_contributors_other',
                'number_of_household_members',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {'marital_status': admin.VERTICAL,
                    'ethnicity': admin.VERTICAL,
                    'highest_education': admin.VERTICAL,
                    'current_occupation': admin.VERTICAL,
                    'provides_money': admin.VERTICAL,
                    'money_earned': admin.VERTICAL,
                    'contributes_to_expenses': admin.VERTICAL,
                    'socio_demo_changed': admin.VERTICAL}

    filter_horizontal = ('expense_contributors',)

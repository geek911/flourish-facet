from django.contrib import admin
from ...admin_site import flourish_facet_admin
from ...models import MaternalHivArt
from ...forms import MaternalHivArtForm
from edc_model_admin import audit_fieldset_tuple
from ..modeladmin_mixins import CrfModelAdminMixin


@admin.register(MaternalHivArt, site=flourish_facet_admin)
class MaternalHivArtAdmin(CrfModelAdminMixin):
    form = MaternalHivArtForm

    fieldsets = (
        (None, {
            'fields': (
                'facet_visit',
                'report_datetime',
            )
        }),
        ('Mothers living with HIV', {
            "fields": (
                'hiv_test_date',
                'art_received',
                'drug_combination_before',
                'drug_combination_before_other',
                'art_start_date',
                'art_received_preg',
                'drug_combination_during',
                'drug_combination_during_other',
                'art_switch',
                'art_regimen',
                'art_regimen_other',
                'art_regimen_start',
                'reason_regimen_change',
                'reason_regimen_change_other',
                'art_challenges',
                'art_challenges_other'
            )
        }),
        ('HIV -Negative mothers', {
            'fields': (
                'father_hiv',
                'father_hiv_no',
                'father_hiv_dont',
                'comment',
                'hiv_result_father',
                'hiv_test_date_father',
                'father_art',
                'father_art_start',
                'hiv_status_disclosure',
                'hiv_status_disclosure_reaction',
                'comment_end',

            )
        }), audit_fieldset_tuple
    )

    radio_fields = {
        'art_received': admin.VERTICAL,
        'drug_combination_before': admin.VERTICAL,
        'art_received_preg': admin.VERTICAL,
        'drug_combination_during': admin.VERTICAL,
        'art_switch': admin.VERTICAL,
        'art_regimen': admin.VERTICAL,
        'reason_regimen_change': admin.VERTICAL,
        'father_hiv': admin.VERTICAL,
        'father_hiv_no': admin.VERTICAL,
        'father_hiv_dont': admin.VERTICAL,
        'hiv_result_father': admin.VERTICAL,
        'father_art': admin.VERTICAL,
        'hiv_status_disclosure': admin.VERTICAL,
    }

    filter_horizontal = (
        'art_challenges', 'hiv_status_disclosure_reaction'
    )

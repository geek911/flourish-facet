from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class FlourishConsentListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        position=1,
        lookup={})

    pregnant_mothers = ListboardFilter(
        label='Pregnant Mothers',
        position=2,
        lookup={'caregiverchildconsent__child_dob__isnull': True})

    age_0_to_2_months = ListboardFilter(
        label='Age 0 to 2 months',
        position=3,
        lookup={'caregiverchildconsent__child_dob': 'age_0_to_2_months'}
    )

    age_2_to_4_months = ListboardFilter(
        label='Age 2 to 4 months',
        position=4,
        lookup={}
    )

    age_4_to_6_months = ListboardFilter(
        label='Age 4 to 6 months',
        position=5,
        lookup={}
    )

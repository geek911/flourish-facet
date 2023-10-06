from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

app_label = 'flourish_facet'


@register()
class FacetGAD7ReferralRuleGroup(CrfRuleGroup):

    facet_gad_anxiety_referral_fu = CrfRule(
        predicate=P('referred_to', 'eq', 'receiving_emotional_care'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.facetcaregivergadreferralfu'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.facetcaregivergadreferral'

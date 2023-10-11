from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
from edc_constants.constants import YES
from edc_metadata import NOT_REQUIRED, REQUIRED

app_label = 'flourish_facet'


@register()
class IntimatePartnerViolenceReferralRuleGroup(CrfRuleGroup):
    intimate_partner_violence_referral = CrfRule(
        predicate=P('referral', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.intimatepartnerviolencereferral']
    )

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.intimatepartnerviolence'

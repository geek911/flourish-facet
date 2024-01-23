from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
from ..predicates import MaternalPredicates


app_label = 'flourish_facet'
pc = MaternalPredicates()


@register()
class MaternalVisitRuleGroup(CrfRuleGroup):

    facet_maternalhivart = CrfRule(
        predicate=pc.func_hiv_positive,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.maternalhivart'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.facetvisit'

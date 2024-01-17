from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
from ..predicates import ChildPredicates


app_label = 'flourish_facet'
pc = ChildPredicates()


@register()
class ChildVisitRuleGroup(CrfRuleGroup):

    facet_child_hiv_test = CrfRule(
        predicate=pc.func_hiv_exposed,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.childhivtesting'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.facetvisit'

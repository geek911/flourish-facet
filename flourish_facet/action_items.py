from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, site_action_items, HIGH_PRIORITY

FACET_MOTHER_OFFSTUDY_ACTION = 'submit-mother-facet-offstudy'

FACET_CHILD_OFFSTUDY_ACTION = 'submit-child-facet-offstudy'

class FacetMotherOffStudyAction(Action):
    name = FACET_MOTHER_OFFSTUDY_ACTION
    display_name = 'Submit FACET Offstudy'
    reference_model = 'flourish_facet.facetmotheroffschedule'
    admin_site_name = 'flourish_facet_admin'
    priority = HIGH_PRIORITY
    show_on_dashboard = True


class FacetChildOffStudyAction(Action):
    name = FACET_CHILD_OFFSTUDY_ACTION
    display_name = 'Submit FACET Offstudy'
    reference_model = 'flourish_facet.facetchildoffschedule'
    admin_site_name = 'flourish_facet_admin'
    priority = HIGH_PRIORITY
    show_on_dashboard = True

site_action_items.register(FacetMotherOffStudyAction)

site_action_items.register(FacetChildOffStudyAction)


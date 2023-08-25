from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

mother_schedule = Schedule(
    name='mother_facet_schedule',
    verbose_name='Mother FACET Schedule',
    onschedule_model='flourish_facet.onschedulefacetmother',
    offschedule_model='flourish_facet.motheroffschedule')


child_schedule = Schedule(
    name='child_facet_schedule',
    verbose_name='Child FACET Schedule',
    onschedule_model='flourish_facet.onschedulefacetchild',
    offschedule_model='flourish_facet.childoffschedule')
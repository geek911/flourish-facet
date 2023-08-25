from edc_base.utils import relativedelta
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Crf, Requisition, FormsCollection
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Visit
from .crfs import mother_crfs, child_crfs
from .schedules import mother_schedule, child_schedule


mother_visit_schedule = VisitSchedule(
    name='mother_visit_schedule1',
    verbose_name='Mother FACET Schedule',
    death_report_model='flourish_facet.facetdeathreport',
    offstudy_model='flourish_facet.onschedulefacetmother',
    visit_model='flourish_facet.facetvisit')



child_visit_schedule = VisitSchedule(
    name='child_visit_schedule1',
    verbose_name='Child FACET Schedule',
    death_report_model='flourish_facet.facetdeathreport',
    offstudy_model='flourish_facet.onschedulefacetchild',
    visit_model='flourish_facet.facetvisit')


mother_visit_schedule.add_schedule(mother_schedule)
child_visit_schedule.add_schedule(child_schedule)
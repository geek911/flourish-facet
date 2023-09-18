from edc_base.utils import relativedelta
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Crf, Requisition, FormsCollection
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Visit
from .crfs import mother_crfs, child_crfs
from .schedules import mother_schedule, child_schedule
from edc_visit_schedule.models import SubjectScheduleHistory

mother_visit_schedule = VisitSchedule(
    name='f_mother_visit_schedule',
    verbose_name='Mother FACET Schedule',
    death_report_model='flourish_facet.facetdeathreport',
    offstudy_model='flourish_facet.facetmotheroffschedule',
    locator_model='flourish_caregiver.caregiverlocator'
)

mother_visit_schedule.add_schedule(mother_schedule)

child_visit_schedule = VisitSchedule(
    name='f_child_visit_schedule',
    verbose_name='Child FACET Schedule',
    death_report_model='flourish_facet.facetdeathreport',
    offstudy_model='flourish_facet.facetchildoffschedule',
    locator_model=''

)


child_visit_schedule.add_schedule(child_schedule)


site_visit_schedules.register(mother_visit_schedule)
site_visit_schedules.register(child_visit_schedule)
# site_visit_schedules.
from dateutil.relativedelta import relativedelta
from edc_visit_schedule.visit import Visit
from .crfs import mother_crfs, child_crfs
from .schedules import mother_schedule, child_schedule

mother_visit = Visit(
    code='2600F',
    title='Visit 2600F',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    crfs=mother_crfs,
    facility_name='5-day clinic')

child_visit = Visit(
    code='2600F',
    title='Visit 2600F',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    crfs=child_crfs,
    facility_name='5-day clinic')

mother_schedule.add_visit(mother_visit)
child_schedule.add_visit(child_visit)

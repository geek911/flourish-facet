from dateutil import relativedelta
from edc_visit_schedule.visit import Visit
from .crfs import mother_crfs, child_crfs
from .schedules import mother_schedule, child_schedule

mother_visit = Visit(
    code='2600F',
    title='Visit 2600F',
    timepoint=0,
    rbase=relativedelta(days=0),
    crfs=mother_crfs)

child_visit = Visit(
    code='2600F',
    title='Visit 2600F',
    timepoint=0,
    rbase=relativedelta(days=28),
    crfs=child_crfs)

mother_schedule.add_visit(mother_schedule)
child_schedule.add_visit(child_visit)
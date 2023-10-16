from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow, get_uuid
from edc_visit_schedule import site_visit_schedules


def age_in_months(dob):
    today = get_utcnow().today()
    delta = relativedelta(today, dob)
    months = delta.months + (delta.years * 12)

    return months


def get_facet_child_schedule():
    _, child_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
        onschedule_model='flourish_facet.onschedulefacetchild',
        name='child_facet_schedule')
    return child_schedule


def get_facet_mother_schedule():
    _, mother_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
        onschedule_model='flourish_facet.onschedulefacetmother',
        name='mother_facet_schedule')

    return mother_schedule

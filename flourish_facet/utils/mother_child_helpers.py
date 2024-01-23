from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow, get_uuid, age
from edc_visit_schedule import site_visit_schedules
from django.apps import apps as django_apps


def child_age_in_months(reference_date, subject_identifier):

    facet_consent_model = django_apps.get_model('flourish_facet.facetconsent')
    try:
        facet_consent_obj = facet_consent_model.objects.filter(
            subject_identifier=subject_identifier
        ).latest('consent_datetime')

    except:
        pass
    else:

        child_consents = facet_consent_obj.motherchildconsent_set.all()

        ages = []

        for consent in child_consents:

            if consent.child_dob:

                delta = age(consent.child_dob, reference_date)

                months = (delta.years * 12) + delta.months

                ages.append(str(months))
            else:
                ages.append("0")

        return ", ".join(ages)


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

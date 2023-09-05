
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from edc_visit_schedule import site_visit_schedules
from edc_base.utils import age, get_utcnow
from .mother import FacetConsent
from .child import MotherChildConsent


@receiver(post_save, weak=False, sender=FacetConsent,
          dispatch_uid='facet_consent_on_post_save')
def facet_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put mother on schedule
    """

    _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
        onschedule_model='flourish_facet.onschedulefacetmother',
        name='mother_facet_schedule'
    )

    schedule.put_on_schedule(
        subject_identifier = instance.subject_identifier, 
        schedule_name = 'mother_facet_schedule'
    )
    


@receiver(post_save, weak=False, sender=MotherChildConsent,
          dispatch_uid='facet_child_consent_on_post_save')
def facet_child_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put child on schedule
    """

    child_age = age(instance.child_dob, get_utcnow().date())

    if child_age.years == 0 and child_age.months <= 6:

        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model='flourish_facet.onschedulefacetchild',
            name='child_facet_schedule'
        )

        schedule.put_on_schedule(
            subject_identifier = instance.subject_identifier, 
            schedule_name = 'child_facet_schedule'
        )
        
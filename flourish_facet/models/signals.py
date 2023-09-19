
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db import transaction
from edc_visit_schedule import site_visit_schedules
from edc_base.utils import age, get_utcnow
from edc_constants.constants import POS
from .mother import FacetConsent
from .child import MotherChildConsent
from .child import ChildHivTesting
from ..models import FacetChildOffSchedule, FacetMotherOffSchedule
from ..action_items import FacetChildOffStudyAction
from ..utils import trigger_action_item
from ..action_items import FACET_MOTHER_OFFSTUDY_ACTION, FACET_CHILD_OFFSTUDY_ACTION


@receiver(post_save, weak=False, sender=FacetConsent,
          dispatch_uid='facet_consent_on_post_save')
def facet_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put mother on schedule
    """

    with transaction.atomic():
        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model='flourish_facet.onschedulefacetmother',
            name='mother_facet_schedule'
        )

        schedule.put_on_schedule(
            subject_identifier=instance.subject_identifier,
            schedule_name='mother_facet_schedule'
        )


@receiver(post_save, weak=False, sender=MotherChildConsent,
          dispatch_uid='facet_consent_on_post_save')
def facet_child_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put child on schedule
    """
    with transaction.atomic():

        _, child_schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model='flourish_facet.onschedulefacetchild',
            name='child_facet_schedule'
        )

        child_schedule.put_on_schedule(
            subject_identifier=instance.subject_identifier,
            schedule_name='child_facet_schedule'
        )


@receiver(post_save, weak=False, sender=ChildHivTesting,
          dispatch_uid='child_hiv_testing_on_post_save')
def facet_child_hiv_testing_on_post_save(sender, instance, raw, created, **kwargs):

    if instance.hiv_result_6_weeks == POS:
        child_subject_identifier = instance.facet_visit.subject_identifier

        trigger_action_item(
            model_cls=FacetChildOffSchedule,
            action_name=FACET_CHILD_OFFSTUDY_ACTION,
            subject_identifier=child_subject_identifier,
            repeat=False,
        )


def get_mother_subject_identifier(child_subject_identifier):

    try:

        child_cosnent = MotherChildConsent.objects.filter(
            subject_identifier=child_subject_identifier
        ).latest('consent_datetime')

    except MotherChildConsent.DoesNotExist:
        raise Exception('Mother consent does not exist')
    else:
        return child_cosnent.facet_consent.subject_identifier


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


@receiver(post_save, weak=False, sender=FacetChildOffSchedule,
          dispatch_uid='facet_child_off_schedule_on_post_save')
def facet_child_off_schedule_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put child off-schedule
    """
    with transaction.atomic():

        subject_identifier = instance.subject_identifier

        child_schedule = get_facet_child_schedule()

        if child_schedule.is_onschedule(subject_identifier=subject_identifier,
                                        report_datetime=instance.report_datetime):

            child_schedule.take_off_schedule(
                subject_identifier=subject_identifier,
                offschedule_datetime=instance.report_datetime)


@receiver(post_save, weak=False, sender=FacetMotherOffSchedule,
          dispatch_uid='facet_mother_off_schedule_on_post_save')
def facet_mother_off_schedule_on_post_save(sender, instance, raw, created, **kwargs):
    """
    - Put mother off-schedule
    """
    with transaction.atomic():

        subject_identifier = instance.subject_identifier

        schedule = get_facet_mother_schedule()

        if schedule.is_onschedule(subject_identifier=subject_identifier,
                                  report_datetime=instance.report_datetime):

            schedule.take_off_schedule(
                subject_identifier=subject_identifier,
                offschedule_datetime=instance.report_datetime)

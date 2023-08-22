from django.db import models
from edc_visit_tracking.model_mixins import VisitModelMixin, CaretakerFieldsMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager as BaseCurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_fields.custom_fields import OtherCharField
from edc_reference.model_mixins import ReferenceModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from flourish_facet.models.child.child_appointment import Appointment
from ...choices import VISIT_INFO_SOURCE, VISIT_REASON, ALIVE_DEAD_UNKNOWN, \
    INFO_PROVIDER, VISIT_STUDY_STATUS
from edc_constants.constants import ALIVE
from edc_visit_tracking.managers import VisitModelManager


class CurrentSiteManager(VisitModelManager, BaseCurrentSiteManager):
    pass


class FacetChildVisit(VisitModelMixin, CreatesMetadataModelMixin,
                      ReferenceModelMixin, RequiresConsentFieldsModelMixin,
                      CaretakerFieldsMixin, SiteModelMixin, BaseUuidModel):

    """ A model completed by the user on child visits. """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='Reason for visit',
        max_length=25,
        choices=VISIT_REASON)

    reason_missed = models.CharField(
        verbose_name=(
            'If \'missed\' above, reason scheduled '
            'scheduled visit was missed'),
        blank=True,
        null=True,
        max_length=250)

    information_provider = models.CharField(
        verbose_name=(
            'Please indicate who provided most of the information for this child\'s visit'),
        max_length=20,
        choices=INFO_PROVIDER)

    information_provider_other = OtherCharField(
        verbose_name='If Other, specify',
        max_length=25,
        blank=True,
        null=True)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        blank=True,
        null=True,
        max_length=25)

    study_status = models.CharField(
        verbose_name="What is the participant's current study status",
        max_length=50,
        choices=VISIT_STUDY_STATUS)

    survival_status = models.CharField(
        max_length=10,
        verbose_name='Participant\'s survival status',
        choices=ALIVE_DEAD_UNKNOWN,
        null=True,
        default=ALIVE)

    info_source = models.CharField(
        verbose_name='Source of information?',
        max_length=25,
        choices=VISIT_INFO_SOURCE)

    on_site = CurrentSiteManager()

    objects = VisitModelManager()

    history = HistoricalRecords()

    class Meta(VisitModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = "Facet Child Visit"
        verbose_name_plural = "Facet Child Visit"

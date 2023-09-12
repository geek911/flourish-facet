from django.db import models
from flourish_caregiver.models.list_models import EmoSupportType, EmoHealthImproved
from flourish_caregiver.choices import EMO_SUPPORT_PROVIDER
from ..model_mixins import ReferralFUFormMixin
from flourish_facet.models.model_mixins.crf_model_mixin import CrfModelMixin


class FacetCaregiverEdinburghReferralFU(ReferralFUFormMixin, CrfModelMixin):

    emo_support_provider = models.CharField(
        verbose_name=('You mentioned that you are currently receiving emotional '
                      'support services. Do you mind sharing with us where you are receiving '
                      'these services?'),
        max_length=40,
        choices=EMO_SUPPORT_PROVIDER)

    emo_support_type = models.ManyToManyField(
        EmoSupportType,
        related_name='facet_emo_support_type',
        verbose_name=(
            'If yes, what kind of emotional support did you receive?'),
        blank=True)

    emo_health_improved = models.ManyToManyField(
        EmoHealthImproved,
        related_name='facet_emo_health_improved',
        verbose_name=('Since you received emotional support, how has your emotional health '
                      'improved?'),
        blank=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Caregiver Edinburgh Referral Follow Up Form'
        verbose_name_plural = 'Caregiver Edinburgh Referral Follow Up Form'

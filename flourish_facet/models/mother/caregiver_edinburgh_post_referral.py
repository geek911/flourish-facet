from django.db import models
from flourish_caregiver.models.list_models import EmoSupportType, EmoHealthImproved
from ..model_mixins import ReferralFUFormMixin
from flourish_facet.models.model_mixins.crf_model_mixin import CrfModelMixin


class FacetCaregiverEdinburghPostReferral(ReferralFUFormMixin, CrfModelMixin):

    emo_support_type = models.ManyToManyField(
        EmoSupportType,
        related_name='facet_post_emo_support_type',
        verbose_name=(
            'If yes, what kind of emotional support did you receive?'),
        blank=True)

    emo_health_improved = models.ManyToManyField(
        EmoHealthImproved,
        related_name='facet_post_emo_health_improved',
        verbose_name=('Since you received emotional support, how has your emotional health '
                      'improved?'),
        blank=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Caregiver Edinburgh Post Referral Form'
        verbose_name_plural = 'Caregiver Edinburgh Post Referral Forms'

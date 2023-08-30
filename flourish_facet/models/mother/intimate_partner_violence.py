from django.db import models
from ..model_mixins import CrfModelMixin
from ...choices import OCCURENCES_MORE


class IntimatePartnerViolence(CrfModelMixin):

    physically_hurt = models.CharField(
        verbose_name='How often does your partner physically hurt you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )

    insult_talk = models.CharField(
        verbose_name='How often does your partner physically hurt you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )
    threaten = models.CharField(
        verbose_name='How often does your partner physically hurt you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )
    scream_curse = models.CharField(
        verbose_name='How often does your partner physically hurt you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Intimate Partner Violence'
        verbose_name_plural = 'Intimate Partner Violence'

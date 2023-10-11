from django.db import models
from ..model_mixins import CrfModelMixin
from ...choices import OCCURENCES_MORE
from edc_constants.choices import YES_NO_NA


class IntimatePartnerViolence(CrfModelMixin):

    physically_hurt = models.CharField(
        verbose_name='How often does your partner physically hurt you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )

    insult_talk = models.CharField(
        verbose_name='How often does your partner insult or talk down to you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )
    threaten = models.CharField(
        verbose_name='How often does your partner threaten you with harm?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )
    scream_curse = models.CharField(
        verbose_name='How often does your partner scream or curse at you?',
        choices=OCCURENCES_MORE,
        max_length=20,
    )

    referral = models.CharField(
        verbose_name='Do you need a referral?',
        choices=YES_NO_NA,
        max_length=5,
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Intimate Partner Violence'
        verbose_name_plural = 'Intimate Partner Violence'

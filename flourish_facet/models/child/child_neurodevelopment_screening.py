from django.db import models
from ..model_mixins import CrfModelMixin
from edc_constants.choices import YES_NO


class ChildNeurodevelopmentScreening(CrfModelMixin):

    can_move_eyes = models.CharField(
        verbose_name='Can the child move eyes or head in the direction of sounds',
        choices=YES_NO,
        max_length=5,

    )
    can_respond_sound = models.CharField(
        verbose_name='Can the child respond by making sounds when spoken to',
        choices=YES_NO,
        max_length=5,

    )
    can_eyes_move = models.CharField(
        verbose_name='Can the child eyes move well together (no squint)',
        choices=YES_NO,
        max_length=5,

    )
    can_recognize = models.CharField(
        verbose_name='Can the child recognize familiar faces',
        choices=YES_NO,
        max_length=5,

    )
    can_laugh = models.CharField(
        verbose_name='Can the child laugh aloud',
        choices=YES_NO,
        max_length=5,

    )
    can_use_sounds = models.CharField(
        verbose_name='Can the child use different cries or sounds to show hunger,tiredness,discomfort',
        choices=YES_NO,
        max_length=5,
    )
    can_grasp = models.CharField(
        verbose_name='Can the child grasp a toy in each hand',
        choices=YES_NO,
        max_length=5,
    )

    can_lift = models.CharField(
        verbose_name='Can the child lift head when lying on tummy',
        choices=YES_NO,
        max_length=5,

    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Child Neurodevelopment Screening'
        verbose_name_plural = 'Child Neurodevelopment Screening'

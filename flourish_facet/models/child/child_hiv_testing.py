from django.db import models
from ..model_mixins import CrfModelMixin
from ...choices import AGE_BREASTFEEDING_ENDED, POS_NEG_IND, YES_NO_DNK, REASON_CHILD_NOT_TESTED
from ...action_items import FACET_CHILD_OFFSTUDY_ACTION
from edc_base.model_fields import OtherCharField
from edc_action_item.model_mixins import ActionModelMixin


class ChildHivTesting(CrfModelMixin):

    child_tested = models.CharField(
        verbose_name='Has your child ever been tested for HIV ?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 4 , If yes go to question 6'
    )

    reason_not_tested = models.CharField(
        verbose_name='What is the reason your child has never been tested for HIV?',
        max_length=35,
        choices=REASON_CHILD_NOT_TESTED
    )

    reason_not_tested_other = OtherCharField()

    child_tested_6_weeks = models.CharField(
        verbose_name='Was your child tested for HIV at their 6-week visit?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 8 , If yes go to question 7'
    )

    hiv_result_6_weeks = models.CharField(
        verbose_name="What was your child’s HIV test result at 6 weeks",
        choices=POS_NEG_IND,
        blank=True,
        max_length=15,
        help_text='If Positive, take off-study , If Negative go to question 10')

    reason_not_tested_6_weeks = models.CharField(
        max_length=35,
        choices=REASON_CHILD_NOT_TESTED,
        verbose_name="If your child was not tested for HIV at their 6-week visit, what was the reason? "
    )
    reason_not_tested_6_weeks_other = OtherCharField()

    child_breastfed = models.CharField(
        verbose_name='Have you ever breastfed your child?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 12 , If yes go to question 11'
    )

    child_breastfeeding = models.CharField(
        verbose_name='Are you currently still breatfeeding your child ?',
        max_length=15,
        null=True,
        blank=True,
        choices=YES_NO_DNK,
    )

    child_breastfed_end = models.CharField(
        verbose_name=(
            'If you already stopped breastfeeding your child,''How old was your child when you stopped breastfeeding?'),
        choices=AGE_BREASTFEEDING_ENDED,
        max_length=20,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Child HIV Testing'
        verbose_name_plural = 'Child HIV Testing'

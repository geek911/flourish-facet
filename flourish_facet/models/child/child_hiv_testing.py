from django.db import models
from ..model_mixins import CrfModelMixin
from ...choices import AGE_BREASTFEEDING_ENDED, POS_NEG_IND, YES_NO_DNK


class ChildHivTesting(CrfModelMixin):

    child_tested = models.CharField(
        verbose_name='Has your child ever been tested for HIV ?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 4 , If yes go to question 5'
    )

    reason_not_tested = models.TextField(
        verbose_name='What isthe reason your child has never been tested for HIV?',
        max_length=250,
        blank=True,
        null=True,
    )

    child_tested_6_weeks = models.CharField(
        verbose_name='Was your child tested for HIV at their 6-week visit?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 7 , If yes go to question 6'
    )

    hiv_result_6_weeks = models.CharField(
        verbose_name="What was your child’s HIV test result at 6 weeks",
        choices=POS_NEG_IND,
        max_length=15,
        help_text='If Positive, take off-study , If Negative go to question 8')

    reason_not_tested_6_weeks = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="If your child was not tested for HIV at their 6-week visit, what was the reason? "
    )

    child_breastfed = models.CharField(
        verbose_name='Have you ever breastfed your child?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 13 , If yes go to question 9'
    )

    child_breastfeeding = models.CharField(
        verbose_name='Are you currently still breatfeeding your child ?',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 13 ,If yes go to question 10'
    )
    child_breastfed_tested = models.CharField(
        verbose_name='If your child is breastfeeding ,have they been tested for HIV at the last 3 months',
        max_length=15,
        choices=YES_NO_DNK,
        help_text='If no, go to question 12 , If yes go to question 11'
    )

    child_breastfed_tested_result = models.CharField(
        verbose_name=(
            'If your child is breastfeeding and they were tested for HIV in the last 3 months,'' what was their result?'),
        choices=POS_NEG_IND,
        max_length=15,
        help_text='If Positive, take off-study , If Negative End form'
    )

    reason_not_tested_3_months = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="If your child was not tested in the last 3 months, what was the reason? "
    )

    child_breastfed_end = models.CharField(
        verbose_name=(
            'If you already stopped breastfeeding your child,''How old was your child when you stopped breastfeeding?'),
        choices=AGE_BREASTFEEDING_ENDED,
        max_length=20,
        help_text='End form'
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Child HIV Testing'
        verbose_name_plural = 'Child HIV Testing'

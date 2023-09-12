from django.db import models
from ..model_mixins import CrfModelMixin
from edc_base.model_validators.date import date_not_future
from edc_base.utils import age, get_utcnow


class InfantBehaviourQuestionnaire(CrfModelMixin):

    dob = dob = models.DateField(
        verbose_name='Child Date of Birth',
        help_text="Must match labour and delivery report.",
        validators=[date_not_future, ])

    child_age = models.IntegerField(
        verbose_name='Child age in weeks?',
        help_text='(Weeks)',
        blank=False)

    @property
    def child_age(self):
        child_age = age(self.dob, get_utcnow())
        return child_age.weeks

    def save(self, *args, **kwargs):

        child_age = self.child_age
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Infant Behaviour Questionnaire'
        verbose_name_plural = 'Infant Behaviour Questionnaire'

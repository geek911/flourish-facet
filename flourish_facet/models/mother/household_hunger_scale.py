from django.db import models
from ...choices import OCCURENCES
from .model_mixins.crf_model_mixin import CrfModelMixin


class HouseholdHungerScale(CrfModelMixin):

    no_food = models.CharField(
        verbose_name="In the past 4 weeks (30 days),was there ever no food to eat of any kind in your household ?",
        choices=OCCURENCES,
        max_length=20,
    )

    no_food_night = models.CharField(
        verbose_name="In the past 4 weeks (30 days),did you or any household member go to sleep at night hungry?",
        choices=OCCURENCES,
        max_length=20,
    )
    no_food_day_night = models.CharField(
        verbose_name=("In the past 4 weeks (30 days),"
                      "did you or any household member go a whole day and night without eating?"),
        choices=OCCURENCES,
        max_length=20,
    )

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Household Hunger Scale'
        verbose_name_plural = 'Household Hunger Scale'

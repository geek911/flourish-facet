from flourish_caregiver.models.model_mixins import SocioDemographicDataMixin, HouseHoldDetailsMixin
from ..model_mixins import CrfModelMixin
from edc_base.model_mixins import BaseUuidModel
from ..list_models import ExpenseContributors
from django.db import models


class FacetSocioDemographicData(SocioDemographicDataMixin, CrfModelMixin):
    """ A model completed by the user on Demographics form for all mothers.
    """

    expense_contributors = models.ManyToManyField(
        ExpenseContributors,
        verbose_name='Who in the household contributes to supporting the family '
                     'expenses:',
        blank=True
    )

    stay_with_child = None

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = "Socio Demographic Data"
        verbose_name_plural = "Socio Demographic Data"

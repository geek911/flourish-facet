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

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = "Socio Demographic Data"
        verbose_name_plural = "Socio Demographic Data"


class FacetHouseHoldDetails(HouseHoldDetailsMixin, BaseUuidModel):
    """ Applicable for twins living in different households.
    """

    parent_model_attr = 'facet_socio_demographics_data'

    socio_demographics_data = models.ForeignKey(
        FacetSocioDemographicData, on_delete=models.CASCADE)

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = 'Household Details'
        verbose_name_plural = 'Household Details'
        unique_together = (
            'socio_demographics_data', 'child_identifier',)

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from flourish_child.choices import (
    WATER_SOURCE, COOKING_METHOD, TOILET_FACILITY, HOUSE_TYPE,
    HIGHEST_EDUCATION)
from flourish_child.choices import ETHNICITY, SCHOOL_TYPE

from flourish_child.models.model_mixins import ChildSocioDemographicMixin

from ..model_mixins import CrfModelMixin


class FacetChildSocioDemographic(ChildSocioDemographicMixin, CrfModelMixin):

    """ A model completed by the user on Demographics form for all infants.
    """

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = "Facet Child Sociodemographic Data"
        verbose_name_plural = "Child Sociodemographic Data"

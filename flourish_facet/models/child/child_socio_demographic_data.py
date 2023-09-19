from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from flourish_child.choices import (
    WATER_SOURCE, COOKING_METHOD, TOILET_FACILITY, HOUSE_TYPE)
from flourish_child.choices import ETHNICITY, SCHOOL_TYPE

from flourish_child.models.model_mixins import ChildSocioDemographicMixin

from flourish_facet.choices import HIGHEST_EDUCATION
from ..model_mixins import CrfModelMixin


class FacetChildSocioDemographic(ChildSocioDemographicMixin, CrfModelMixin):

    """ A model completed by the user on Demographics form for all infants.
    """
    stay_with_caregiver = models.CharField(
        verbose_name='Is the infant/child/adolescent currently living with '
                     'the caregiver who is also participating in the FACET'
                     ' study?',
        choices=YES_NO,
        max_length=3)

    education_level = models.CharField(
        verbose_name='What level/class of school is the child currently in?',
        max_length=20,
        choices=HIGHEST_EDUCATION,
        default='no_schooling')

    class Meta:
        app_label = 'flourish_facet'
        verbose_name = "Facet Child Sociodemographic Data"
        verbose_name_plural = "Child Sociodemographic Data"

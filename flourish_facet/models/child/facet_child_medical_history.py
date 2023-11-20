from django.db import models
from flourish_child.models.model_mixins import ChildMedicalHistoryMixin
from ..model_mixins import CrfModelMixin
from ..list_models import ChronicConditions, GeneralSymptoms, Medications


class FacetChildMedicalHistory(CrfModelMixin,
                               ChildMedicalHistoryMixin):
    """A model completed by the user on Medical History for all children."""

    child_chronic = models.ManyToManyField(
        ChronicConditions,
        related_name='chronic_conditions',
        verbose_name=('Does the Child have any of the above. '
                      'Tick all that apply'),)

    current_symptoms = models.ManyToManyField(
        GeneralSymptoms,
        verbose_name="What are your child's current symptoms",
        blank=True,
    )

    current_medications = models.ManyToManyField(
        Medications,
        verbose_name='What medications does your child currently take',
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Children Medical History'
        verbose_name_plural = 'Children Medical History'

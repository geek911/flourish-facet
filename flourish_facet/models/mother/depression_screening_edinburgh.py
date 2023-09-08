from flourish_caregiver.models.model_mixins import CaregiverEdinburghDeprScreeningMixin
from ..model_mixins import CrfModelMixin

class DepressionScreeningEdinBurgh(CaregiverEdinburghDeprScreeningMixin, CrfModelMixin):
    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = "Depression Screening - EdinBurgh"
        verbose_name_plural = "Depression Screening - EdinBurgh"
from flourish_caregiver.models.model_mixins import CaregiverPhqDeprScreeningMixin
from ..model_mixins import CrfModelMixin


class DepressionScreeningPhq9(CaregiverPhqDeprScreeningMixin, CrfModelMixin):
    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = "Depression Screening - PHQ9"
        verbose_name_plural = "Depression Screening - PHQ9"

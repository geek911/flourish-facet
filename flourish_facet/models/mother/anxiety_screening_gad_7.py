from flourish_caregiver.models.model_mixins import CaregiverGadAnxietyScreeningMixin
from ..model_mixins import CrfModelMixin

class AnxietyScreeningGad7(CaregiverGadAnxietyScreeningMixin, CrfModelMixin):
    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = "Anxiety Screening GAD-7"
        verbose_name_plural = "Anxiety Screening GAD-7"
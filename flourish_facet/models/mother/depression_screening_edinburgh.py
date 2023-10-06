from flourish_caregiver.models.model_mixins import CaregiverEdinburghDeprScreeningMixin
from ..model_mixins import CrfModelMixin


class DepressionScreeningEdinBurgh(CaregiverEdinburghDeprScreeningMixin, CrfModelMixin):

    def save(self, *args, **kwargs):
        self.depression_score = self.calculate_depression_score()
        super().save(*args, **kwargs)

    def calculate_depression_score(self):
        score = 0
        for f in self._meta.get_fields():
            if f.name in ['depressed_mood', 'guilt_feelings', 'suicidal',
                          'insomnia_initial', 'insomnia_middle',
                          'insomnia_delayed', 'work_interests', 'retardation',
                          'agitation', 'anxiety_pyschic', 'anxiety',
                          'gastro_symptoms', 'general_symptoms',
                          'genital_symptoms', 'hypochondriasis', 'weight_loss',
                          'insight', ]:
                score += int(getattr(self, f.name))
        return score

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = "Depression Screening - EdinBurgh"
        verbose_name_plural = "Depression Screening - EdinBurgh"

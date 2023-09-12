from ..model_mixins import ReferralFormMixin
from flourish_facet.models.model_mixins.crf_model_mixin import CrfModelMixin


class FacetCaregiverEdinburghReferral(ReferralFormMixin, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Caregiver Edinburgh Referral Form'
        verbose_name_plural = 'Caregiver Edinburgh Referral Form'

from ..model_mixins import CrfModelMixin, ReferralFUFormMixin


class FacetCaregiverPhqPostReferral(ReferralFUFormMixin, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'PHQ-9 Post Referral Form'
        verbose_name_plural = 'PHQ-9 Post Referral Forms'

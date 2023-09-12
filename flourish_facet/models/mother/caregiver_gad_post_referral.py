
from ..model_mixins import CrfModelMixin, ReferralFUFormMixin


class FacetCaregiverGadPostReferral(ReferralFUFormMixin, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Caregiver GAD-7 Post Referral Form'
        verbose_name_plural = 'Caregiver GAD-7 Post Referral Forms'

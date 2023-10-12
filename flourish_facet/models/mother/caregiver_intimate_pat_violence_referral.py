from ..model_mixins import CrfModelMixin, ReferralFormMixin


class IntimatePartnerViolenceReferral(ReferralFormMixin, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Intimate Partner Violence Referral Form for Caregivers'
        verbose_name_plural = 'Intimate Partner Violence Form for Caregiver'

from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class ArtChallenges(ListModelMixin, BaseUuidModel):
    pass


class PartnerReaction(ListModelMixin, BaseUuidModel):
    pass


class ExpenseContributors(ListModelMixin, BaseUuidModel):
    pass

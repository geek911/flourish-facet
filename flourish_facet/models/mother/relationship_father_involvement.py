from django.db import models
from flourish_caregiver.models.list_models import HouseholdMember
from flourish_caregiver.models.model_mixins import RelationshipFatherInvolvementMixin
from flourish_facet.models.model_mixins.crf_model_mixin import CrfModelMixin


class FacetRelationshipFatherInvolvement(RelationshipFatherInvolvementMixin, CrfModelMixin):
    """A CRF to be completed by biological mothers living with HIV,
    at the 6 month visit
    """
    read_books = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_read_books',
        verbose_name='Read books or looked at picture books with your child', )

    told_stories = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_told_stories',
        verbose_name='Told stories to your child', )

    sang_songs = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_sang_songs',
        verbose_name='Sang songs to or with your child, including lullabies', )

    took_child_outside = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_took_child_outside',
        verbose_name='Took your child outside the home', )

    played_with_child = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_played_with_child',
        verbose_name='Played with your child', )

    named_with_child = models.ManyToManyField(
        HouseholdMember,
        related_name='facet_named_with_child',
        verbose_name='Named, counted, or drew things with or for your child', )

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_facet'
        verbose_name = 'Relationship and Father Involvement'
        verbose_name_plural = 'Relationship and Father Involvement'

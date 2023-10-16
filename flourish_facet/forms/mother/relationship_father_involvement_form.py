from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from flourish_facet.form_validators.relationship_father_involvement_form_validation import FacetRelationshipFatherInvolvementFormValidator

from ...models import FacetRelationshipFatherInvolvement


class FacetRelationshipFatherInvolvementForm(SiteModelFormMixin, FormValidatorMixin,
                                             forms.ModelForm):

    form_validator_cls = FacetRelationshipFatherInvolvementFormValidator

    class Meta:
        model = FacetRelationshipFatherInvolvement
        fields = '__all__'

from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from flourish_form_validations.form_validators import RelationshipFatherInvolvementFormValidator
from ...models import FacetRelationshipFatherInvolvement


class FacetRelationshipFatherInvolvementForm(SiteModelFormMixin, FormValidatorMixin,
                                             forms.ModelForm):

    form_validator_cls = RelationshipFatherInvolvementFormValidator

    class Meta:
        model = FacetRelationshipFatherInvolvement
        fields = '__all__'

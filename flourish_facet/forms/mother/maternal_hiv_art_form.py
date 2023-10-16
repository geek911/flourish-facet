from django import forms
from ...models import MaternalHivArt
from edc_base.sites import SiteModelFormMixin
from ...form_validators import MaternalHivArtFormValidator
from edc_form_validators import FormValidatorMixin


class MaternalHivArtForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = MaternalHivArtFormValidator

    class Meta:
        model = MaternalHivArt
        fields = '__all__'

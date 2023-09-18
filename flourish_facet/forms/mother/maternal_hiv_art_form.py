from django import forms
from ...models import MaternalHivArt
from edc_base.sites import SiteModelFormMixin
from ...form_validators import MaternalHivArtFormValidator


class MaternalHivArtForm(SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = MaternalHivArtFormValidator

    class Meta:
        model = MaternalHivArt
        fields = '__all__'

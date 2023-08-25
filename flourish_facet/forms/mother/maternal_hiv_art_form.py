from django import forms
from ...models import MaternalHivArt
from edc_base.sites import SiteModelFormMixin


class MaternalHivArtForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalHivArt
        fields = '__all__'

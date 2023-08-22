from django import forms
from ...models import ChildHivTesting


class ChildHivTestingForm(forms.ModelForm):

    class Meta:
        model = ChildHivTesting
        fields = '__all__'

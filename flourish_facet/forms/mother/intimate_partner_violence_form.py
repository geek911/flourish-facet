from django import forms
from ...models import IntimatePartnerViolence


class IntimatePartnerViolenceForm(forms.ModelForm):

    class Meta:
        model = IntimatePartnerViolence
        fields = '__all__'

from django import forms

from ..form_mixins import SubjectModelFormMixin
from ...models import DepressionScreeningEdinBurgh


class DepressionScreeningEdinBurghForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = DepressionScreeningEdinBurgh
        fields = '__all__'

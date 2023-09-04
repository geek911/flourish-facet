from django import forms

from ..form_mixins import SubjectModelFormMixin
from ...models import DepressionScreeningPhq9


class DepressionScreeningPhq9Form(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = DepressionScreeningPhq9
        fields = '__all__'

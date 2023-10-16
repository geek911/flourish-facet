from django import forms

from ..form_mixins import SubjectModelFormMixin
from ...models import AnxietyScreeningGad7


class AnxietyScreeningGad7Form(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = AnxietyScreeningGad7
        fields = '__all__'

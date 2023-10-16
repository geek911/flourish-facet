from django import forms
from edc_base.sites import SiteModelFormMixin
from flourish_facet.form_validators.infant_behaviour_questionnaire_validation import InfantBehaviourQuestionnaireFormValidator
from flourish_facet.models.child.infant_behaviour_questionnaire import InfantBehaviourQuestionnaire
from edc_form_validators import FormValidatorMixin
from django.apps import apps as django_apps


class InfantBehaviourQuestionnaireForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = InfantBehaviourQuestionnaireFormValidator

    child_birth_model = 'flourish_child.childbirth'

    @property
    def child_birth_model_cls(self):
        return django_apps.get_model(self.child_birth_model)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        child_subject_identifier = self.initial.get('subject_identifier', None)

        child_birth_obj = self.child_birth_model_cls.objects.filter(
            subject_identifier=child_subject_identifier).first()
        if child_birth_obj:
            if child_birth_obj.dob:
                self.initial['dob'] = child_birth_obj.dob

    class Meta:
        model = InfantBehaviourQuestionnaire
        fields = '__all__'

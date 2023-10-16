from flourish_form_validations.form_validators import RelationshipFatherInvolvementFormValidator
from flourish_caregiver.helper_classes import MaternalStatusHelper
from django.apps import apps as django_apps
from django.forms import ValidationError


class FacetRelationshipFatherInvolvementFormValidator(RelationshipFatherInvolvementFormValidator):
    maternal_visit_model = 'flourish_caregiver.maternalvisit'

    @property
    def maternal_visit_model_cls(self):
        return django_apps.get_model(self.maternal_visit_model)

    @property
    def maternal_status_helper(self):
        facet_visit = self.cleaned_data.get('facet_visit')
        subject_identifier = facet_visit.subject_identifier
        maternal_visit = self.maternal_visit_model_cls.objects.filter(
            subject_identifier=subject_identifier).latest('report_datetime')
        if maternal_visit:
            return MaternalStatusHelper(maternal_visit)

    @property
    def has_delivered(self):
        facet_visit = self.cleaned_data.get('facet_visit')
        subject_identifier = facet_visit.subject_identifier
        maternal_visit = self.maternal_visit_model_cls.objects.filter(
            subject_identifier=subject_identifier).latest('report_datetime')
        onschedule_model = self.onschedule_model(instance=maternal_visit)
        model_cls = self.onschedule_model_cls(onschedule_model)
        try:
            model_obj = model_cls.objects.get(
                subject_identifier=subject_identifier,
                schedule_name=maternal_visit.schedule_name)
        except model_cls.DoesNotExist:
            raise ValidationError('Onschedule does not exist.')
        else:
            child_subject_identifier = model_obj.child_subject_identifier
            if self.is_preg_enrol(child_subject_identifier):
                return self.maternal_delivery_model_cls.objects.filter(
                    subject_identifier=subject_identifier).exists()
            return True

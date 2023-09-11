from django.apps import apps as django_apps
from django.forms import ValidationError
from edc_constants.constants import OTHER, YES
from edc_form_validators import FormValidator


class SocioDemographicDataFormValidator(FormValidator):
    antenatal_enrollment_model = 'flourish_caregiver.antenatalenrollment'
    preg_women_screening_model = 'flourish_caregiver.screeningpregwomen'
    delivery_model = 'flourish_caregiver.maternaldelivery'
    maternal_dataset_model = 'flourish_caregiver.maternaldataset'
    child_socio_demographic_model = 'flourish_child.childsociodemographic'

    @property
    def maternal_dataset_cls(self):
        return django_apps.get_model(self.maternal_dataset_model)

    @property
    def antenatal_enrollment_cls(self):
        return django_apps.get_model(self.antenatal_enrollment_model)

    @property
    def preg_screening_cls(self):
        return django_apps.get_model(self.preg_women_screening_model)

    @property
    def delivery_model_cls(self):
        return django_apps.get_model(self.delivery_model)

    @property
    def child_socio_demographic_cls(self):
        return django_apps.get_model(self.child_socio_demographic_model)

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'facet_visit').subject_identifier
        super().clean()

        self.required_if(
            YES,
            field='contributes_to_expenses',
            field_required='expense_contributors')

        self.m2m_other_specify(
            OTHER,
            m2m_field='expense_contributors',
            field_other='expense_contributors_other',
        )

        other_specify_fields = ['marital_status', 'ethnicity',
                                'current_occupation', 'provides_money',
                                'money_earned', 'toilet_facility']
        for field in other_specify_fields:
            self.validate_other_specify(field=field)

    @property
    def is_from_prev_study(self):
        facet_visit = self.cleaned_data.get('facet_visit')

        return self.maternal_dataset_cls.objects.filter(
            subject_identifier=facet_visit.subject_identifier).exists()

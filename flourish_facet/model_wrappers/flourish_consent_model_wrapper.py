
from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper
from .facet_screening_model_wrapper import FacetScreeningModelWrapper
from .facet_consent_model_wrapper import FacetConsentModelWrapper
from ..models import FacetSubjectScreening, FacetConsent


class FlourishConsentModelWrapper(ModelWrapper):
    model = 'flourish_caregiver.subjectconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'facet_flourish_consent_listboard_url')
    next_url_attrs = ['subject_identifier',]
    facet_screening_model = 'flourish_facet.facetsubjectscreening'
    facet_consent_model = 'flourish_facet.facetconsent'
    

    @property
    def facet_screening_cls(self):
        return django_apps.get_model(self.facet_screening_model)

    @property
    def facet_consent_cls(self):
        return django_apps.get_model(self.facet_consent_model)

    @property
    def facet_screening_obj(self):
        try:
            obj = self.facet_screening_cls.objects.filter(
                subject_identifier=self.object.subject_identifier
            ).latest('report_datetime')
        except self.facet_screening_cls.DoesNotExist:
            pass
        else:
            return obj

    @property
    def facet_consent_obj(self):
        try:
            obj = self.facet_consent_cls.objects.filter(
                subject_identifier=self.object.subject_identifier
            ).latest('report_datetime')
        except self.facet_consent_cls.DoesNotExist:
            pass
        else:
            return obj

    @property
    def facet_screening_wrapper(self):

        facet_screening_obj = self.facet_screening_obj or FacetSubjectScreening(
            subject_identifier=self.object.subject_identifier
        )

        return FacetScreeningModelWrapper(model_obj=facet_screening_obj)

    @property
    def facet_consent_wrapper(self):

        facet_consent_obj = self.facet_consent_obj or FacetConsent(
            subject_identifier=self.object.subject_identifier
        )

        return FacetConsentModelWrapper(model_obj=facet_consent_obj)

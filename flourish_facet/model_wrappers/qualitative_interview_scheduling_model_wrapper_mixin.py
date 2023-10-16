from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .qualitative_interview_scheduling_model_wrapper import QualitativeInterviewSchedulingModelWrapper


class QualitativeInterviewSchedulingModelWrapperMixin:

    qualitative_interview_scheduling_model_wrapper_cls = QualitativeInterviewSchedulingModelWrapper

    @property
    def qualitative_interview_scheduling_model_obj(self):
        """Returns a qualitative interview scheduling instance or None.
        """
        try:
            return self.qualitative_interview_scheduling_cls.objects.get(
                **self.qualitative_interview_scheduling_options)
        except ObjectDoesNotExist:
            return None

    @property
    def qualitative_interview_scheduling(self):
        """"Returns a wrapped saved or unsaved qualitative interview scheduling
         """
        model_obj = self.qualitative_interview_scheduling_model_obj or \
            self.qualitative_interview_scheduling_cls(
                **self.create_qualitative_interview_scheduling_options)
        return self.qualitative_interview_scheduling_model_wrapper_cls(model_obj=model_obj)

    @property
    def qualitative_interview_scheduling_cls(self):
        return django_apps.get_model('flourish_facet.qualitativeinterviewscheduling')

    @property
    def create_qualitative_interview_scheduling_options(self):
        """Returns a dictionary of options to create a new
        unpersisted qualitative interview scheduling model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

    @property
    def qualitative_interview_scheduling_options(self):
        """Returns a dictionary of options to get an existing
        qualitative interview scheduling model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

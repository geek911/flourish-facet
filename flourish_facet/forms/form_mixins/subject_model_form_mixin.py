from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.crf_date_validator import CrfDateValidator
from edc_visit_tracking.crf_date_validator import (
    CrfReportDateAllowanceError, CrfReportDateBeforeStudyStart)
from edc_visit_tracking.crf_date_validator import CrfReportDateIsFuture

from ...models import FacetVisit


class SubjectModelFormMixin(SiteModelFormMixin, FormValidatorMixin,
                            forms.ModelForm):

    visit_model = FacetVisit

    visit_attr = None

    def clean(self):
        cleaned_data = super().clean()
        if (cleaned_data.get('facet_visit', None)
                and cleaned_data.get('facet_visit').visit_code):
            if cleaned_data.get('report_datetime'):
                try:
                    CrfDateValidator(
                        report_datetime=cleaned_data.get('report_datetime'),
                        visit_report_datetime=cleaned_data.get(
                            self._meta.model.visit_model_attr()).report_datetime)
                except (CrfReportDateAllowanceError, CrfReportDateBeforeStudyStart,
                        CrfReportDateIsFuture) as e:
                    raise forms.ValidationError(e)
        return cleaned_data


class InlineSubjectModelFormMixin(FormValidatorMixin, forms.ModelForm):

    visit_model = FacetVisit

from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO
from django.core.exceptions import ValidationError


class QualitativeInterviewSchedulingFormValidator(FormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')
        super().clean()
        self.validate_google_calendar_sheet(cleaned_data=self.cleaned_data)
        self.validate_google_calendar_sheet_unverified(
            cleaned_data=self.cleaned_data)
        self.validate_google_calendar_sheet_incomplete(
            cleaned_data=self.cleaned_data)

    def validate_google_calendar_sheet(self, cleaned_data=None):
        google_sheet_calendar = cleaned_data.get('google_sheet_calendar')
        complete = cleaned_data.get('complete')

        if google_sheet_calendar == YES and complete == 'incomplete':
            raise ValidationError("You’ve indicated that the participant has been added to the "
                                  "Google sheet calendar.Please save the form as complete.")

    def validate_google_calendar_sheet_unverified(self, cleaned_data=None):
        google_sheet_calendar = cleaned_data.get('google_sheet_calendar')
        complete = cleaned_data.get('complete')

        if google_sheet_calendar == YES and complete == 'unverified':
            raise ValidationError("You’ve indicated that the participant has been added to the "
                                  "Google sheet calendar.Please save the form as complete.")

    def validate_google_calendar_sheet_incomplete(self, cleaned_data=None):
        google_sheet_calendar = cleaned_data.get('google_sheet_calendar')
        complete = cleaned_data.get('complete')

        if google_sheet_calendar == NO and complete == 'complete':
            raise ValidationError("You’ve indicated that the participant has not been added to the "
                                  "Google sheet calendar. Please save the form as incomplete "
                                  "Once the participant is added to the Google Sheet calendar,"
                                  "return to this form and save the form as complete")

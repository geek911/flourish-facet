
from edc_identifier.subject_identifier import SubjectIdentifier as BaseSubjectIdentifier


class FocusGroupIdentifier(BaseSubjectIdentifier):

    template = '{protocol_number}-{sequence}'
    label = 'groupidentifier'

    def __init__(self, group_type=None, **kwargs):
        self.group_type = group_type
        super().__init__(**kwargs)

    @property
    def identifier(self):
        """Returns a new and unique identifier and updates
        the IdentifierModel.
        """
        if not self._identifier:
            breakpoint()
            self._identifier = self.template.format(**self.template_opts)
            check_digit = self.checkdigit.calculate_checkdigit(
                ''.join(self._identifier.split('-')))
            if self.group_type:
                self._identifier = f'{self.group_type}{self._identifier}-{check_digit}'
            self.identifier_model = self.identifier_model_cls.objects.create(
                name=self.label,
                sequence_number=self.sequence_number,
                identifier=self._identifier,
                protocol_number=self.protocol_number,
                device_id=self.device_id,
                model=self.requesting_model,
                site=self.site,
                identifier_type=self.identifier_type)
        return self._identifier

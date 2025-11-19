from input_validation import validate_reference
from repositories.reference_repository import reference_repository
from entities.reference import Reference
from entities.field import Field

class ReferenceService:
    def __init__(self, reference_repository=reference_repository):
        self._reference_repository = reference_repository

    def get_references(self):
        return self._reference_repository.get_references()

    def create_reference(self, reference_type, reference_name, fields):
        validate_reference(reference_type, reference_name, fields)
        # create field objects
        fields = [Field(name, value) for name, value in fields.items()]

        # create reference object
        reference = Reference(reference_type, reference_name, fields)
        return self._reference_repository.create_reference(reference)

reference_service = ReferenceService()

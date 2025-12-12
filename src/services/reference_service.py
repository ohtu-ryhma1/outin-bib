from src.models.reference import Reference
from src.repositories.reference_repository import (
    ReferenceRepository,
    reference_repository,
)
from src.services.reference_types import get_reference_fields
from src.services.reference_validation import validate_reference


class ReferenceService:
    def __init__(self, repo: ReferenceRepository):
        self._repo = repo

    def get_all(self) -> list:
        return self._repo.get_all()

    def get_all_meta(
        self, key: str = None, types: list = None, field_filters: list = None
    ) -> list:
        refs = self._repo.get_all(key, types, field_filters)
        for ref in refs:
            ref.required, ref.optional = get_reference_fields(ref.type)
            ref.required_count = len([f for f in ref.fields if f.type in ref.required])
            ref.optional_count = len([f for f in ref.fields if f.type in ref.optional])

        return refs

    def get(self, ref_id: id = None) -> Reference:
        return self._repo.get(ref_id)

    def get_meta(self, ref_id: id = None) -> Reference:
        ref = self._repo.get(ref_id)
        ref.required, ref.optional = get_reference_fields(ref.type)
        ref.required_count = len([f for f in ref.fields if f.type in ref.required])
        ref.optional_count = len([f for f in ref.fields if f.type in ref.optional])

        return ref

    def create(self, ref_data: dict) -> Reference:
        validate_reference(ref_data)
        return self._repo.create(ref_data)

    def update(self, ref_id: int, ref_data: dict) -> Reference:
        validate_reference(ref_data)
        return self._repo.update(ref_id, ref_data)

    def delete_all(self):
        return self._repo.delete_all()


# default service
reference_service = ReferenceService(reference_repository)

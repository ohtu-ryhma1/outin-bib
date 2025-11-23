from typing import Iterable

from sqlalchemy import ScalarResult

from src.models.reference import Reference
from src.repositories.reference_repository import reference_repository
from src.services.input_validation import validate_reference


class ReferenceService:
    def __init__(self, repo):
        self._repo = repo

    def get_all(self) -> Iterable[ScalarResult]:
        return self._repo.get_all()

    def get(self, ref_id: id = None) -> Reference:
        return self._repo.get(ref_id)

    def create(self, ref_data: dict) -> Reference:
        validate_reference(ref_data)
        return self._repo.create(ref_data)

    def update(self, ref_id: int, ref_data: dict) -> Reference:
        validate_reference(ref_data)
        return self._repo.update(ref_id, ref_data)


# default service
reference_service = ReferenceService(reference_repository)

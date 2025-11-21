from services.input_validation import validate_reference
from models.reference import Reference
from repositories.reference_repository import reference_repository
from typing import Iterable
from sqlalchemy import ScalarResult


class ReferenceService:
    def __init__(self, repo):
        self._repo = repo

    def get_all(self) -> Iterable[ScalarResult]:
        return self._repo.get_all()

    def create(self, ref_data: dict) -> Reference:
        validate_reference(ref_data)
        return self._repo.create(ref_data)


# default service
reference_service = ReferenceService(reference_repository)

from repositories.reference_repository import reference_repository
from entities.reference import Reference
from entities.field import Field

class ReferenceService:
    def __init__(self, repo):
        self._repo = repo

    def get_all(self) -> Iterable[ScalarResult]:
        return self._repo.get_all()

    def create(self, ref_data: dict) -> Reference:
        return self._repo.create(ref_data)

# default service
reference_service = ReferenceService(reference_repository)

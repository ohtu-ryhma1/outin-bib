from typing import Iterable
from sqlalchemy import ScalarResult

from config import db
from sqlalchemy import select

from models.reference import Reference
from models.field import Field


class ReferenceRepository:

    def __init__(self, db):
        self._db = db

    def get_all(self) -> Iterable[ScalarResult]:
        references = self._db.session.execute(select(Reference)).scalars()
        return references

    def create(self, ref_data: dict) -> Reference:
        reference = Reference(
            type=ref_data["type"],
            name=ref_data["name"]
        )

        for field_type, field_value in ref_data["fields"].items():
            reference.fields.append(Field(
                type=field_type,
                value=field_value
            ))

        self._db.session.add(reference)
        self._db.session.commit()

        return reference


# default repository
reference_repository = ReferenceRepository(db)

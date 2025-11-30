from sqlalchemy import select

from src.config import db
from src.models.field import Field
from src.models.reference import Reference


class ReferenceRepository:

    def __init__(self, database):
        self._db = database

    def get_all(self) -> list:
        refs = self._db.session.scalars(select(Reference))
        return list(refs)

    def get(self, ref_id: int = None) -> Reference:
        if not ref_id:
            ref = self._db.session.scalar(select(Reference))
        else:
            ref = self._db.session.scalar(
                select(Reference).where(Reference.id == ref_id)
            )

        if not ref and not ref_id:
            raise LookupError("There are no references in this repository")
        if not ref:
            raise LookupError(f"Reference with id {ref_id} does not exist")

        return ref

    def create(self, ref_data: dict) -> Reference:
        ref = Reference(
            type=ref_data["type"],
            name=ref_data["name"],
        )

        for field_type, field_value in ref_data["fields"].items():
            ref.fields.append(
                Field(
                    type=field_type,
                    value=field_value,
                )
            )

        self._db.session.add(ref)
        self._db.session.commit()

        return ref

    def update(self, ref_id: int, ref_data: dict) -> Reference:
        ref = self.get(ref_id)

        ref.type = ref_data["type"]
        ref.name = ref_data["name"]

        ref.fields.clear()

        for field_type, field_value in ref_data["fields"].items():
            ref.fields.append(
                Field(
                    type=field_type,
                    value=field_value,
                )
            )

        self._db.session.commit()

        return ref

    def delete_all(self):
        refs = self._db.session.scalars(select(Reference))
        for ref in refs:
            self._db.session.delete(ref)
        self._db.session.commit()
        return True


# default repository
reference_repository = ReferenceRepository(db)

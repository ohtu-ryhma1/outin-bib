from sqlalchemy import and_, select
from sqlalchemy.exc import IntegrityError

from src.config import db
from src.models.field import Field
from src.models.reference import Reference


class ReferenceRepository:

    def __init__(self, database):
        self._db = database

    def get_all(
        self, key: str = None, types: list = None, field_filters: list = None
    ) -> list:
        stmt = self._query(key, types, field_filters)
        refs = self._db.session.scalars(stmt)
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
            key=ref_data["key"],
        )

        for field_type, field_value in ref_data["fields"].items():
            ref.fields.append(
                Field(
                    type=field_type,
                    value=field_value,
                )
            )

        try:
            self._db.session.add(ref)
            self._db.session.commit()
        except IntegrityError:
            self._db.session.rollback()

    def update(self, ref_id: int, ref_data: dict) -> Reference:
        ref = self.get(ref_id)

        ref.type = ref_data["type"]
        ref.key = ref_data["key"]

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

    def _query(self, key=None, types=None, field_filters=None):
        stmt = select(Reference)

        if key:
            stmt = stmt.where(Reference.key.contains(key))

        if types:
            stmt = stmt.where(Reference.type.in_(types))

        if field_filters:
            for field_type, field_value in field_filters:
                stmt = stmt.where(
                    Reference.fields.any(
                        and_(
                            Field.type == field_type, Field.value.contains(field_value)
                        )
                    )
                )

        return stmt


# default repository
reference_repository = ReferenceRepository(db)

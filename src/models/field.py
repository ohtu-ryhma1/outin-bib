from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.config import db


class Field(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    value: Mapped[str]

    reference_id: Mapped[int] = mapped_column(db.ForeignKey("reference.id"))
    reference: Mapped["Reference"] = relationship(back_populates="fields")

    def __repr__(self) -> str:
        return f"Field(id={self.id!r}, type={self.type!r}, value={self.value!r})"

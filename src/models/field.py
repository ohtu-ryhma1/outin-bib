from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from config import db

class Field(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    value: Mapped[str]

    reference: Mapped["Reference"] = relationship(back_populates="fields")

    def __repr__(self) -> str:
        return f"Field(id={self.id!r}, type={self.type!r}, value={self.value!r})"
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from typing import List

from config import db


class Reference(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str] = mapped_column(unique=True)

    fields: Mapped[List["Field"]] = relationship(back_populates="reference")

    def __repr__(self) -> str:
        return f"Reference(id={self.id!r}, type={self.type!r}, name={self.name!r})"
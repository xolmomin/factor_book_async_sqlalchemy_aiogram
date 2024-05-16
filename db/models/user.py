from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from db.base import CreatedModel


class User(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(255))
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

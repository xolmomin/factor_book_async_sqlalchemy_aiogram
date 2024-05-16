from sqlalchemy import BigInteger, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.base import CreatedModel


class Category(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    products: Mapped[list['Product']] = relationship('Product', back_populates='category')


class Product(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    price: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    category_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(Category.id, ondelete='CASCADE'))
    category: Mapped['Category'] = relationship('Category', back_populates='products')

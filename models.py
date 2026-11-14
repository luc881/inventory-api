from decimal import Decimal
from sqlalchemy import Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"                        # the table this class maps to

    id: Mapped[int] = mapped_column(primary_key=True) # INTEGER PRIMARY KEY
    name: Mapped[str]                                 # TEXT NOT NULL
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))  # NUMERIC(10, 2) NOT NULL
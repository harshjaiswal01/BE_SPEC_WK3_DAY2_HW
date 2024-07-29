from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Products(Base):
    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(db.String(255), nullable = False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)


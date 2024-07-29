from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
# from models.order import Orders

class Customer(Base):
    __tablename__ = "Customer" #MAke your class name the same as your table name

    #mapping class attributes to database table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(db.String(75), nullable = False)
    email: Mapped[str] = mapped_column(db.String(300))
    phone: Mapped[str] = mapped_column(db.String(16))
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(db.ForeignKey('Roles.id'))

    role: Mapped['Role'] = db.relationship()

    #Creating one to many relationship to Orders table
    orders: Mapped[List["Orders"]] = db.relationship(back_populates = 'customer') #back_populates insures that both ends of the relationship have access to the other

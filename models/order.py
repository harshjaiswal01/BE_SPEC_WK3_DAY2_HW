from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
# from models.product import Products
# from models.customer import Customer
from datetime import date, timedelta
from models.orderProduct import order_products

# class Orders(Base):
#     __tablename__ = "Orders"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
#     customer_id: Mapped[int] = mapped_column(db.ForeignKey("Customer.id")) #This is Foreign Key which is referencing customer table
#     expected_delivery_date: Mapped[date] = mapped_column(db.Date, nullable=True)

#     #creating a many to one relationship to Customer table
#     customer: Mapped["Customer"] = db.relationship(back_populates = "orders")

#     #creating a many to many relationship to Products through our association table order_products
#     products: Mapped[List["Products"]] = db.relationship(secondary=order_products)

# order_products = db.Table(
#     "Order_Products",
#     Base.metadata, #Allows this table to locate the foreign keys from other base classes
#     db.Column("order_id", db.ForeignKey("Orders.id"), primary_key = True),
#     db.Column("product_id", db.ForeignKey("Products.id"), primary_key = True)
# )

order_products = db.Table(
    "Order_Products",
    db.Model.metadata,
    db.Column("order_id", db.ForeignKey("Orders.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("Products.id"), primary_key=True),
    extend_existing=True
)

class Orders(Base):
    __tablename__ = "Orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("Customer.id"))
    expected_delivery_date: Mapped[date] = mapped_column(db.Date, nullable=True)
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    products: Mapped[List["Products"]] = relationship("Products", secondary=order_products)

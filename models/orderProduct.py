from database import db, Base

order_products = db.Table(
    "Order_Products",
    Base.metadata, #Allows this table to locate the foreign keys from other base classes
    db.Column("order_id", db.ForeignKey("Orders.id"), primary_key = True),
    db.Column("product_id", db.ForeignKey("Products.id"), primary_key = True)
)
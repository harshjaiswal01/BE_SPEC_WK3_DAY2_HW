from datetime import date, timedelta
from werkzeug.security import generate_password_hash
from database import db
from models.customer import Customer
from models.order import Orders
from models.product import Products
from models.role import Role

def add_sample_data():
    # Create sample roles
    admin_role = Role(role_name="Admin")
    user_role = Role(role_name="User")

    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()

    # Create sample customers
    customer1 = Customer(
        customer_name="John Doe",
        email="john.doe@example.com",
        phone="1234567890",
        username="johndoe",
        password="password123",
        role_id=user_role.id
    )

    customer2 = Customer(
        customer_name="Jane Smith",
        email="jane.smith@example.com",
        phone="0987654321",
        username="janesmith",
        password="password456",
        role_id=admin_role.id
    )

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.commit()

    # Create sample products
    product1 = Products(
        product_name="Bread",
        price=2.99
    )

    product2 = Products(
        product_name="Cake",
        price=15.99
    )

    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

    # Create sample orders
    order1 = Orders(
        order_date=date.today(),
        customer_id=customer1.id,
        expected_delivery_date=date.today() + timedelta(days=7)
    )

    order2 = Orders(
        order_date=date.today(),
        customer_id=customer2.id,
        expected_delivery_date=date.today() + timedelta(days=7)
    )

    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    # Associate products with orders
    order1.products.append(product1)
    order1.products.append(product2)
    order2.products.append(product1)

    db.session.commit()

    print("Sample data added successfully.")

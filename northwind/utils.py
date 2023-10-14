from faker import Faker
from .models import *
import random
import datetime
from .random_data import designations, categories, bool_data, title_of_courtesy, regions

fake = Faker("en_IN")


def generate_suppliers(num):
    Supplier.objects.all().delete()
    for i in range(num):
        supplier = Supplier(
            company_name=fake.company(),
            contact_name=fake.name(),
            contact_title=random.choice(designations),
            address=fake.street_address(),
            city=fake.city(),
            region=fake.state(),
            postal_code=fake.postcode(),
            country=fake.country(),
            phone=fake.phone_number(),
        )
        supplier.save()


def generate_category():
    Category.objects.all().delete()
    for i in categories:
        category = Category(name=i, description=fake.paragraph(nb_sentences=5))
        category.save()


def generate_products(num):
    Product.objects.all().delete()
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()

    for i in range(num):
        product = Product(
            name=f"product_{random.randint(1, 500)}",
            supplier=random.choice(suppliers),
            category=random.choice(categories),
            quantity_per_unit=random.randint(1, 20),
            unit_price=random.randint(110, 998) / 100,
            units_in_stock=random.randint(1, 20),
            units_on_order=random.randint(1, 20),
            reorder_level=random.randint(1, 8),
            discontinued=random.choice(bool_data),
        )
        product.save()


def generate_customers(num):
    Customer.objects.all().delete()
    for _ in range(num):
        customer = Customer(
            company_name=fake.company(),
            contact_name=fake.name(),
            contact_title=random.choice(designations),
            address=fake.street_address(),
            city=fake.city(),
            region=fake.state(),
            postal_code=fake.postcode(),
            country=fake.country(),
            phone=fake.phone_number(),
            fax=fake.phone_number(),
        )
        customer.save()


def generate_employees(num):
    Employee.objects.all().delete()
    for _ in range(num):
        employee = Employee(
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            title=random.choice(designations),
            title_of_courtesy=random.choice(title_of_courtesy),
            birth_date=fake.date_of_birth(),
            hire_date=fake.date(),
            address=fake.street_address(),
            city=fake.city(),
            region=fake.state(),
            postal_code=fake.postcode(),
            country=fake.country(),
            home_phone=fake.phone_number(),
            extension=fake.phone_number(),
        )
        employee.save()


def generate_employee_reports_to(num):
    employees = Employee.objects.all()
    for _ in range(num):
        employee = Employee(reports_to=random.choice(employees))
        employee.save()


def generate_shippers(num):
    Shipper.objects.all().delete()
    Faker.seed(0)
    for _ in range(num):
        shipper = Shipper(name=fake.name(), phone=fake.phone_number())
        shipper.save()


def generate_regions():
    Region.objects.all().delete()
    for i in regions:
        region = Region(name=i)
        region.save()


def generate_territory(num):
    Territory.objects.all().delete()
    Faker.seed(0)
    regions = Region.objects.all()
    for _ in range(num):
        territory = Territory(name=fake.state(), region=random.choice(regions))
        territory.save()


def generate_employee_territory():
    EmployeeTerritory.objects.all().delete()
    employees = Employee.objects.all()
    territories = Territory.objects.all()
    for i in employees:
        employee_territory = EmployeeTerritory(
            employee=i, territory=random.choice(territories)
        )
        employee_territory.save()


def generate_orders(num):
    Order.objects.all().delete()
    customer = Customer.objects.all()
    employee = Employee.objects.all()
    shippers = Shipper.objects.all()

    for _ in range(num):
        order_date = datetime.datetime.strptime(fake.date(), "%Y-%m-%d")
        required_date = order_date + datetime.timedelta(days=10)
        shipped_date = fake.date_between(order_date, required_date)
        order = Order(
            customer=random.choice(customer),
            employee=random.choice(employee),
            order_date=order_date,
            required_date=required_date,
            shipped_date=shipped_date,
            ship_via=random.choice(shippers),
            freight=random.randint(110, 998) / 100,
            ship_name=fake.name(),
            ship_address=fake.street_address(),
            ship_city=fake.city(),
            ship_region=fake.state(),
            ship_postal_code=fake.postcode(),
            ship_country=fake.country(),
        )
        order.save()


def generate_order_details():
    OrderDetail.objects.all().delete()
    orders = Order.objects.all()
    products = Product.objects.all()
    for i in orders:
        order_details = OrderDetail(
            order=i,
            product=random.choice(products),
            quantity=random.randint(1, 10),
            discount=random.randint(110, 998) / 100,
        )
        order_details.save()

from django.db import models


class Supplier(models.Model):
    company_name = models.CharField(max_length=225)
    contact_name = models.CharField(max_length=225)
    contact_title = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    region = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    fax = models.CharField(max_length=225)
    home_page = models.CharField(max_length=225)

    def __str__(self):
        return self.company_name


class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=225)
    supplier = models.ForeignKey(
        Supplier, related_name="product_supplier", on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        Category, related_name="product_category", on_delete=models.SET_NULL, null=True
    )
    quantity_per_unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    reorder_level = models.IntegerField()
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    company_name = models.CharField(max_length=225)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    title_of_courtesy = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=100)
    extension = models.CharField(max_length=100)
    reports_to = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Shipper(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Territory(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class EmployeeTerritory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    territory = models.ForeignKey(Territory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.employee}-{self.territory}"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="customer_order", on_delete=models.SET_NULL, null=True
    )
    employee = models.ForeignKey(
        Employee, related_name="employee_order", on_delete=models.SET_NULL, null=True
    )
    order_date = models.DateField(null=True, blank=True)
    required_date = models.DateField(null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    ship_via = models.ForeignKey(Shipper, on_delete=models.SET_NULL, null=True)
    freight = models.DecimalField(max_digits=10, decimal_places=3)
    ship_name = models.CharField(max_length=100)
    ship_address = models.CharField(max_length=100)
    ship_city = models.CharField(max_length=100)
    ship_region = models.CharField(max_length=100)
    ship_postal_code = models.CharField(max_length=100)
    ship_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer}-{self.employee}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f"{self.order}-{self.product}"

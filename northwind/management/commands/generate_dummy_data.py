from django.core.management.base import BaseCommand
from ...utils import *


class Command(BaseCommand):
    help = "create dummy data"

    def handle(self, *args, **kwargs):
        generate_suppliers(25)
        generate_category()
        generate_products(150)
        generate_customers(200)
        generate_employees(200)
        generate_employee_reports_to(180)
        generate_shippers(20)
        generate_regions()
        generate_territory(20)
        generate_employee_territory()
        generate_orders(1000)
        generate_order_details()

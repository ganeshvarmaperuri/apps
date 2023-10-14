from django.core.management.base import BaseCommand
from hospital_1.models import *
import random
import datetime
from hospital_1.random_data import *
from faker import Faker

fake = Faker("en_IN")


class Command(BaseCommand):
    help = "create dummy data"

    def handle(self, *args, **kwargs):
        def generate_doctors():
            Doctor.objects.all().delete()
            for _ in range(10):
                doctors = Doctor(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    specialty=random.choice(medical_specializations),
                )
                doctors.save()

        def generate_province():
            Province.objects.all().delete()
            for _ in range(10):
                province = Province(
                    name=fake.state(),
                )
                province.save()

        def generate_patients():
            Patient.objects.all().delete()
            provinces = Province.objects.all()
            for _ in range(100):
                patient = Patient(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birth_date=fake.date_of_birth(),
                    gender=fake.profile()["sex"],
                    allergies=random.choice(allergies),
                    height=random.randint(110, 998) / 100,
                    weight=random.randint(110, 998) / 100,
                    province=random.choice(provinces),
                )
                patient.save()

        def generate_admissions():
            Admission.objects.all().delete()
            patients = Patient.objects.all()
            doctors = Doctor.objects.all()
            admission_date = datetime.datetime.strptime(fake.date(), "%Y-%m-%d")
            discharged_date = fake.date_between(
                admission_date, admission_date + datetime.timedelta(days=100)
            )
            for i in patients:
                admissions = Admission(
                    patient=i,
                    doctor=random.choice(doctors),
                    admission_date=admission_date,
                    discharged_date=discharged_date,
                    diagnosis=random.choice(diagnoses),
                )
                admissions.save()

        generate_doctors()
        generate_province()
        generate_patients()
        generate_admissions()

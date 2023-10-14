from django.db import models
from django.db.models import CharField
from django.db.models.functions import Length

CharField.register_lookup(Length, "length")


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=3)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        related_name="patient_province",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Admission(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.SET_NULL, null=True, blank=True
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        related_name="attending_doctor",
        null=True,
        blank=True,
    )
    admission_date = models.DateField(null=True, blank=True)
    discharged_date = models.DateField(null=True, blank=True)
    diagnosis = models.CharField(max_length=100)

    def __str__(self):
        return self.patient.first_name

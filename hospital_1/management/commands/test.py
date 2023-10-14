from django.core.management.base import BaseCommand
from hospital_1.models import *
from django.db.models import F, Q
from django.db.models.functions import Length
from django.db.models import Count, Case, IntegerField, When
from django.db import connection


class Command(BaseCommand):
    help = "create dummy data"

    def handle(self, *args, **kwargs):
        # print(Province.objects.get(id=17).patient_province.all())
        # same_day_admissions = Admission.objects.filter(admission_date__exact=F('discharged_date'))
        #
        # for i in same_day_admissions:
        #     print(i.admission_date)

        # print(
        #     Patient.objects.filter(
        #         province__name="Odisha", allergies__isnull=False
        #     ).values_list("first_name", "last_name", "allergies")
        # )

        """
        Show unique birth years from patients and order them by ascending.
        """
        # print(Patient.objects.values('birth_date__year').distinct().order_by('birth_date__year'))
        # print(type(Patient.objects.all().first().birth_date.year))

        """
        Show unique first names from the patients table which only occurs once in the list.
        """
        # print(Patient.objects.values_list('first_name').distinct())

        """
        Show patient_id, first_name, last_name from patients who's diagnosis is 'Epilepsy'.
        """
        # print(Patient.objects.filter(admission__diagnosis='Epilepsy').values('first_name', 'last_name'))

        """
        Display every patient's first_name.
        Order the list by the length of each name and then by alphabetically
        """
        # print(
        #     Patient.objects.annotate(name_length=Length("first_name"))
        #     .values_list("first_name")
        #     .order_by("name_length", "first_name")
        # )

        """
        Show patient_id and first_name from patients where their first_name start and ends with 's' and 
        is at least 6 characters long.
        """
        # print(
        #     Patient.objects.filter(
        #         Q(first_name__startswith="s")
        #         & Q(first_name__endswith="s")
        #         & Q(first_name__length__gte=6)
        #     )
        # )

        """
        Show the total amount of male patients and the total amount of female patients in the patients table.
        Display the two results in the same row.
        """
        # print(Patient.objects.aggregate(
        #     male_count=Count(Case(When(gender='M', then=1), output_field=IntegerField())),
        #     female_count=Count(Case(When(gender='F', then=1), output_field=IntegerField())),
        # ))

        """
        Show first and last name, allergies from patients which have allergies to either 'Penicillin' or 'Morphine'. 
        Show results ordered ascending by allergies then by first_name then by last_name.
        """
        # print(
        #     Patient.objects.all()
        #     .filter(allergies__in=["Asthma", "Food Allergies"])
        #     .values("first_name", "last_name", "allergies")
        #     .order_by("allergies", "first_name", "last_name")
        # )

        """
        Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.
        """
        # print(
        #     Admission.objects.values("patient__id", "diagnosis")
        #     .annotate(admission_count=Count("*"))
        #     .filter(admission_count__gt=1)
        # )

        # raw_sql_query = "SELECT patient_id, diagnosis FROM hospital_1_admission GROUP BY patient_id, " \
        #                 "diagnosis HAVING COUNT(*) > 1;"
        # with connection.cursor() as cursor:
        #     cursor.execute(raw_sql_query)
        #     results = cursor.fetchall()
        # print("results", results)
        # for row in results:
        #     patient_id, diagnosis = row
        #     print(f"Patient ID: {patient_id}, Diagnosis: {diagnosis}")

        """
        Show the city and the total number of patients in the city.
        Order from most to least patients and then by city name ascending.
        """
        # print(
        #     Province.objects.annotate(no_of_patients_in_city=Count("patient_province"))
        #     .values("name", "no_of_patients_in_city")
        #     .order_by("-no_of_patients_in_city", "name")
        # )

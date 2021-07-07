from django.core.management.base import BaseCommand, CommandError
import importlib
from myapp.models import Specialty, Company, Vacancy
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('source', nargs='+', type=str)

    def handle(self, *args, source, **options):
        module = importlib.import_module(source[-1])
        for com in module.companies:
            Company.objects.create(
                name=com['title'],
                logo=com['logo'],
                description=com['description'],
                employee_count=com['employee_count']
            )
        for spec in module.specialties:
            Specialty.objects.create(**spec)
        for vac in module.jobs:
            Vacancy.objects.create(
                title=vac['title'],
                specialty_id=vac['specialty'],
                company_id=vac['company'],
                skills=vac['skills'],
                description=vac['description'],
                salary_min=vac['salary_from'],
                salary_max=vac['salary_to'],
                published_at=datetime.strptime(vac['posted'], "%Y-%m-%d")
            )


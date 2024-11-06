import csv
from django.core.management.base import BaseCommand
from catalyst_count.company.models import Company

class Command(BaseCommand):
    help = "Import company data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Company.objects.create(
                    name=row['name'],
                    domain=row['domain'],
                    year_founded=int(row['year founded']) if row['year founded'].isdigit() else None,
                    industry=row['industry'],
                    size_range=row['size range'],
                    locality=row['locality'],
                    country=row['country'],
                    linkedin_url=row['linkedin url'],
                    current_employee_estimate=int(row['current employee estimate']) if row['current employee estimate'].isdigit() else None,
                    total_employee_estimate=int(row['total employee estimate']) if row['total employee estimate'].isdigit() else None,
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported company data'))

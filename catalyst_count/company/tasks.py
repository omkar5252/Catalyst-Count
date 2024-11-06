from celery import shared_task
import csv
from django.core.exceptions import ValidationError
from catalyst_count.company.models import Company

@shared_task(bind=True)
def process_csv(self, file_path):
    """
    Asynchronously processes the uploaded CSV file and saves the data to the database.
    Handles missing fields by setting None or skipping rows with critical missing data.
    """
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            companies = []
            print(reader, '----------reader-----------------------')

            for row in reader:
                # Prepare company data from the CSV row with checks for missing fields
                company_data = {
                    "name": row.get("name", "").strip() or None,
                    "domain": row.get("domain", "").strip() or None,
                    "year_founded": row.get("year founded", "").strip() or None,
                    "industry": row.get("industry", "").strip() or None,
                    "size_range": row.get("size range", "").strip() or None,
                    "locality": row.get("locality", "").strip() or None,
                    "country": row.get("country", "").strip() or None,
                    "linkedin_url": row.get("linkedin url", "").strip() or None,
                    "current_employee_estimate": row.get("current employee estimate", "").strip() or None,
                    "total_employee_estimate": row.get("total employee estimate", "").strip() or None,
                }

                # Handle missing required fields (e.g., name and domain)
                if not company_data["name"] or not company_data["domain"]:
                    print(f"Skipping row with missing required fields: {company_data}")
                    continue  # Skip rows with critical missing data

                # Check if the company already exists based on a unique identifier (e.g., domain)
                if not Company.objects.filter(domain=company_data["domain"]).exists():
                    # Validate and create the company entry
                    try:
                        company = Company(**company_data)
                        company.full_clean()  # Validate model data
                        companies.append(company)
                    except ValidationError as e:
                        self.retry(exc=e, countdown=60)  # Retry on validation error
                        continue  # Skip to the next row
                else:
                    print(f"Skipping duplicate company: {company_data['name']}")

            print(companies, '------companies-----------------------')
            # Bulk create companies in the database
            if companies:
                Company.objects.bulk_create(companies)

        return f"Successfully processed {len(companies)} companies from the CSV file."

    except Exception as e:
        raise self.retry(exc=e, countdown=60)

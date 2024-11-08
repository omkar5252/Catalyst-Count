from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.FloatField(null=True, blank=True)
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    current_employee_estimate = models.IntegerField(null=True, blank=True)
    total_employee_estimate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
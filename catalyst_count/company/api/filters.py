# filters.py
import django_filters
from catalyst_count.company.models import Company

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    domain = django_filters.CharFilter(lookup_expr='icontains')
    industry = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')
    year_founded = django_filters.NumberFilter()
    size_range = django_filters.CharFilter(lookup_expr='icontains')
    current_employee_estimate = django_filters.NumberFilter()
    total_employee_estimate = django_filters.NumberFilter()

    class Meta:
        model = Company
        fields = [
            'name',
            'domain',
            'industry',
            'country',
            'year_founded',
            'size_range',
            'current_employee_estimate',
            'total_employee_estimate',
        ]

from django.contrib.auth.models import User
from .models import School
import django_filters


class SchooFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['Name', 'Address', ]
import django_filters
from django_filters import CharFilter

from .models import *


class RecipeFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['description', 'user']

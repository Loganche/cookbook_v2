from django.shortcuts import render
# Create your views here.
from recipes.models import Recipe


def catalogue(request):
    recipes = Recipe.objects.all()
    return render(request, 'catalogues/catalogue.html', {'recipes': recipes})


def search(request):
    return render(request, 'catalogues/search.html')

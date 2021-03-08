from django.shortcuts import render

# Create your views here.

def catalogue(request):
    return render(request, 'catalogues/catalogue.html')


def search(request):
    return render(request, 'catalogues/search.html')

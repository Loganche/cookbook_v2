from django.shortcuts import render

# Create your views here.

def catalogue(request):
    return render(request, 'accounts/catalogue.html')


def search(request):
    return render(request, 'accounts/search.html')

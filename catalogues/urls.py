from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/', views.catalogue),
    path('search/', views.search),
]

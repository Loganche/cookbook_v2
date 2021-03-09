from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
]

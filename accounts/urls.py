from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('delete/<int:pk>/', views.users, name='delete'),
]

from django.contrib import admin
from django.urls import path
from login_ import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('patient', views.patient, name='patient'),
    path('doctor', views.doctor, name='doctor')
]
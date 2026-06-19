from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokaz_liste, name='url_lista'),
    path('dodaj/', views.zapisz_zadanie, name='url_dodaj'),
    path('edytuj/<int:pk>/', views.zapisz_zadanie, name='url_edytuj'),
    path('usun/<int:pk>/', views.usun_zadanie, name='url_usun'),
]
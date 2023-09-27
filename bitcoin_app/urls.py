from django.urls import path
from . import views

urlpatterns = [
    path('calculate-profit/', views.calculate_profit, name='calculate_profit'),
    # Otras URLs de la aplicación
]

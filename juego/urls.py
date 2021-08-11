from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_preguntas),
    path("ejemplo", views.crear_pregunta)
]
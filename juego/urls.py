from django.urls import path
from . import views

app_name="juego"
urlpatterns = [
    path('', views.listar_preguntas),
    path('preguntas', views.preguntas, name="preguntas"),
    path("detalle_pregunta/<int:identificador>", views.detalle_pregunta, name="detalle_pregunta"),
    path('crear', views.crear_pregunta, name='crear_pregunta'),
    path("editar_pregunta/<int:identificador>", views.editar_pregunta, name="editar_pregunta"),
    path('eliminar/<int:identificador>', views.eliminar_pregunta, name='eliminar'),
    path('confirmar_eliminacion/<int:identificador>', views.confirmar_eliminacion, name='confirmar_eliminacion')

]
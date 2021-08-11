from django import forms
from .models import Respuesta

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Respuesta
        fields = ('id_pregunta', 'opcion', 'puntaje')

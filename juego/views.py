
# Create your views here.
from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta, Partida
from datetime import datetime

from django.contrib.auth.decorators import login_required
from .models import Categoria
# Create your views here.
@login_required(login_url='/login')
def listar_preguntas(request):
    if request.method == "POST":
        resultado = 0
        for i in range(1, 3):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user, fecha=datetime.now, resultado=resultado)
        return redirect("/")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by('?')[:2]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta= item.id)
            categoria = Categoria.objects.get(pk=item.id_categoria.id)
            #{pregunta: {opciones: [opcion1, opcion2, opcionn], categoria: categoria}
            data[item.pregunta]= {'opciones': respuestas, 'categoria': categoria}
        return render(request, 'juego/listar_preguntas.html', {"preguntas": preguntas, "data": data})


@login_required(login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    return render(request, 'juego/crear_pregunta.html', {'form': form})

@login_required(login_url='/login')
def preguntas(request):
    preguntas= Pregunta.objects.all()
    return render(request, 'juego/preguntas.html', {"preguntas": preguntas})


@login_required(login_url='/login')
def detalle_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/detalle_pregunta.html', {"pregunta": pregunta})

from .forms import PreguntaForm
from django.contrib.auth.decorators import permission_required
@login_required(login_url='/login')
@permission_required('juedo.add_pregunta', login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juego:preguntas')
    return render(request, 'juego/crear_pregunta.html', {'form': form})


@login_required(login_url='/login')
def editar_pregunta(request, identificador):
    pregunta= Pregunta.objects.get(pk=identificador)
    if request.method == "POST":
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juego:detalle_pregunta', identificador=item.id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render(request, 'juego/editar_pregunta.html', {'form': form})


@login_required(login_url='/login')
def eliminar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/eliminar_pregunta.html', {"pregunta": pregunta})


@login_required(login_url='/login')
def confirmar_eliminacion(request, identificador):
    Pregunta.objects.get(pk=identificador).delete()
    return redirect("juego:preguntas")


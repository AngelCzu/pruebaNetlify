import time
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import threading
from django.utils import timezone

def agregar_puntos(usuario, cantidad):
    perfil, creado = Puntos.objects.get_or_create(usuario=usuario)
    perfil.puntos += cantidad
    perfil.save()

def agregar_puntos_periodicamente(usuario):
    while True:
        agregar_puntos(usuario, 10)
        time.sleep(60)



def inicio(request):
    salas =  Sala.objects.all()
    num_items = len(salas)

    salas_nombreSala = Sala.objects.filter(nombreSala = 2)
    return render(request, 'inicio.html', {"nomSala":salas, "nom_Sala":salas_nombreSala,"numitems":num_items})

def login_registro(request):
    context = {}  # Define el contexto vacío al principio.

    if request.method == 'POST':
        if 'txtUsuIng' in request.POST and 'txtPasswordIng' in request.POST:
            usuario = request.POST.get('txtUsuIng')
            clave = request.POST.get('txtPasswordIng')
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                # Usuario autenticado con éxito, puedes redirigirlo al inicio u otra página.
                return redirect('/inicio')
            else:
                # Usuario no válido, muestra un mensaje de error en el contexto.
                context['error'] = 'Credenciales inválidas. Intente nuevamente.'

        elif 'txtNomUsuReg' in request.POST and 'txtCorreoReg' in request.POST and 'txtPasswordReg' in request.POST:
            nombre_usuario = request.POST.get('txtNomUsuReg')
            correo = request.POST.get('txtCorreoReg')
            contraseña = request.POST.get('txtPasswordReg')

            # Crea un nuevo usuario
            user = User.objects.create_user(username=nombre_usuario, email=correo, password=contraseña)
            login(request, user)
            agregar_puntos(user, 10)
            # Usuario registrado con éxito, puedes redirigirlo al inicio u otra página.
            return redirect('/inicio')
    # Renderiza la plantilla con el contexto, ya sea que el usuario se autentique o no.
    return render(request, 'login.html', context)

    
@login_required
def perfil(request):
    if request.method == 'POST' and 'logout' in request.POST:
        # Si se envía una solicitud POST con el nombre 'logout', entonces realiza el logout.
        logout(request)
        return redirect('inicio')  # Redirige al usuario a la página de inicio.

    usuario_actual = request.user
    username = usuario_actual.username
    email = usuario_actual.email
    puntos_usuario = Puntos.objects.get(usuario=request.user)
    return render(request, 'perfil.html', {'puntos_usuario': puntos_usuario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Actualiza los datos del usuario
        user = request.user
        user.username = username
        user.email = email
        user.save()

        # Redirige de vuelta al perfil
        return redirect('perfil')

    return render(request, 'editar_perfil.html')
    
def streamStramer(request):
    return render(request, 'streamStramer.html')

def sala_form(request):
    nombre_sala = request.POST.get('txtSala')
    if nombre_sala:
        sala = Sala(nombreSala=nombre_sala)
        sala.save()
        return redirect('/streamStramer')
    return render(request, 'formuSala.html')


def streamViewer(request,nombreSala):
    usuario_actual = request.user

    salas_nombreSala = Sala.objects.get(nombreSala=nombreSala)

    if request.method == 'POST':
        
        mensaje_contenido = request.POST.get('mensaje')
        
        # Guardar el mensaje en la base de datos
        

        mensaje = Mensaje.objects.create(
            sala=salas_nombreSala,
            usuario=usuario_actual,
            contenido=mensaje_contenido,
            timestamp=timezone.now(),
        )
        mensaje.save()

        return redirect('/inicio')  # Redirigir para evitar reenvío del formulario

    # Resto de tu código para obtener puntos, mensajes, etc.
    puntos_usuario = Puntos.objects.get(usuario=request.user)
    mensajes = Mensaje.objects.all()

    return render(request, 'streamViewer.html', {'puntos_usuario': puntos_usuario, 'mensajes': mensajes, 'sala':salas_nombreSala})
from django.shortcuts import render, get_object_or_404
from .models import Categoria, LugarPatrimonial
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def home(request):
    return render(request,'core/home.html')

def catalogo(request):
    data = {}

    data['categorias'] = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        data['lugares'] = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        data['lugares'] = LugarPatrimonial.objects.all()

    return render(request, 'core/catalogo.html', data)

def detalle(request, id):
    data = {}
    data['lugar'] = get_object_or_404(LugarPatrimonial, id=id)

    return render(request, 'core/detalle.html', data)

def iniciar_sesion(request):
    data = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            data['error'] = 'Usuario o contraseña incorrectos'

    return render(request, 'core/login.html', data)

def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect('home') 

@login_required(login_url='login')
@permission_required('core.view_lugarpatrimonial', raise_exception=True)
def gestion(request):
    data = {}
    data['lugares'] = LugarPatrimonial.objects.all()

    return render(request, 'core/gestion.html', data)
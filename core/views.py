from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial

def home(request):
    return render(request,'core/home.html')

def catalogo(request):
    data = {}
    data['lugares'] = LugarPatrimonial.objects.all()


    return render(request, 'core/catalogo.html', data)

def detalle(request, id):
    data = {}
    data['lugar'] = get_object_or_404(LugarPatrimonial, id=id)

    return render(request, 'core/detalle.html', data)
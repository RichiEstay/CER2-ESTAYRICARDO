from django.shortcuts import render
from .models import LugarPatrimonial

def home(request):
    return render(request,'core/home.html')

def catalogo(request):
    data = {}
    data['lugares'] = LugarPatrimonial.objects.all()


    return render(request, 'core/catalogo.html', data)

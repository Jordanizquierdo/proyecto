from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def serie1(request):
    datos = {"nombre":"stranger things","descripcion":"una serie buena","valoracion":"7/10"}
    return render(request, 'app1/pag1.html',datos)
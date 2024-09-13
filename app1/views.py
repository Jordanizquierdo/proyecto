from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def serie1(request):
    datos = {"nombre":"stranger things","descripcion":"una serie buena","valoracion":"7/10","img1":"/static/img/serie1.jfif"}
    return render(request, 'app1/pag.html',datos)

def serie2(request):
    datos = {"nombre":"The Mandalorian","descripcion":"una serie de starwars","valoracion":"9/10","img1":"/static/img/serie2.jfif"}
    return render(request, 'app1/pag.html',datos)

def serie3(request):
    datos = {"nombre":"The Walking Dead","descripcion":"una serie de zombis y personas","valoracion":"3/10","img1":"/static/img/serie3.jfif"}
    return render(request, 'app1/pag.html',datos)
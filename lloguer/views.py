# views.py
from django.shortcuts import render
from .models import Automobil

def mostrar_automobils(request):
    # Recuperar todos los automóviles de la base de datos
    automobils = Automobil.objects.all()
    # Pasar los automóviles a la plantilla para renderizar
    return render(request, 'mostrar_automobils.html', {'automobils': automobils})

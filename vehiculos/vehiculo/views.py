from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculo.html', {'form': form})


@login_required
def listar_vehiculos(request):
    vehiculos_list = Vehiculo.objects.all()
    query = request.GET.get('q')
    precio_condicion = request.GET.get('precio_condicion')

    if query:
        vehiculos_list = vehiculos_list.filter(marca__icontains=query)

    return render(request, 'listar_vehiculos.html', {
        'vehiculos': vehiculos_list,
        'query': query,
    })

from django.shortcuts import render, redirect  
from Aplicacion.models import Cliente, Servicios, Consultas
from Aplicacion.forms import ClienteForm, ServiciosForm, ConsultasForm

def inicio(request):
    return render(request, 'Aplicacion/padre.html')

def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'Aplicacion/servicios.html', {'servicios': servicios})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Aplicacion/clientes.html', {'clientes': clientes})

def consultas(request):
    consultas = Consultas.objects.all()
    return render(request, 'Aplicacion/consultas.html', {'consultas': consultas})

# Formulario para agregar cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'Aplicacion/agregar_cliente.html', {'form': form})

# Formulario para agregar servicio
def agregar_servicio(request):
    if request.method == 'POST':
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServiciosForm()
    return render(request, 'Aplicacion/agregar_servicio.html', {'form': form})

# Formulario para agregar consulta
def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    else:
        form = ConsultasForm()
    return render(request, 'Aplicacion/agregar_consulta.html', {'form': form})

# Formulario de búsqueda y resultados
def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            resultados = Servicios.objects.filter(nombre__icontains=query)
            return render(request, 'Aplicacion/resultados_busqueda.html', {'resultados': resultados})
    return render(request, 'Aplicacion/buscar.html')


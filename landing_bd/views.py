from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models.functions import Lower
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def landing(request):
    return render(request, 'landing_bd\landing.html')

@login_required
def clientes(request):
    clientes = Cliente.objects.annotate(nombre_normalizado=Lower('nombre')).order_by('nombre_normalizado')
    return render(request, 'landing_bd/clientes.html',{
        'clientes' : clientes
    })

@login_required
def familia(request):
    familia = Familia.objects.annotate(nombre_normalizado=Lower('nombre')).order_by('nombre_normalizado')
    return render(request, 'landing_bd/familias.html',{
        'familia' : familia
    })

@login_required
def reuniones(request):
    reuniones = Reuniones.objects.all()
    return render(request, 'landing_bd/reuniones.html',{
        'reuniones' : reuniones
    })

@login_required    
def ejecutivos(request):
    user = User.objects.all()
    return render(request, 'landing_bd/ejecutivos.html',{
        'user' : user
    })

from datetime import date, timedelta

@login_required
def agenda(request):
  hoy = date.today()
  proximos_60_dias = hoy + timedelta(days=60)
  query = request.GET.get('buscar1')
  if query:
    reuniones = Reuniones.objects.filter(fecha__range=[hoy, proximos_60_dias], cliente__nombre__icontains=query)
  else:
    reuniones = Reuniones.objects.filter(fecha__range=[hoy, proximos_60_dias])
  
  return render(request, 'landing_bd/agenda.html', {'reuniones': reuniones})


@login_required
def crear_cliente(request):
    if request.method == 'GET':
        cliente_form = ClienteForm()
        return render(request, 'landing_bd/crear_cliente.html', {
            'cliente_form': cliente_form
            })
    else:
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('clientes')
        else:
            error = "Error: El formulario no es válido. Por favor, revise los errores."
            return render(request, 'landing_bd/crear_cliente.html', {
                'cliente_form': cliente_form, 'error': error
                })


@login_required    
def crear_familia(request): 
    if request.method == 'GET':
        familia_form = FamiliaForm()
        return render(request, 'landing_bd/crear_familia.html', {
            'familia_form' : FamiliaForm
        })
    else:
        familia_form = FamiliaForm(request.POST)
        if familia_form.is_valid():
            familia_form.save()
            return redirect('familia')
        else:
            error = "Error: El formulario no es válido. Por favor, revise los errores."
            return render(request, 'landing_bd/crear_familia.html', {
                'familia_form': familia_form, 'error': error
                })
            
@login_required    
def crear_sociedades(request): 
    if request.method == 'GET':
        sociedades_form = SociedadesForm()
        return render(request, 'landing_bd/crear_sociedades.html', {
            'sociedades_form' : SociedadesForm
        })
    else:
        sociedades_form = SociedadesForm(request.POST)
        if sociedades_form.is_valid():
            sociedades_form.save()
            return redirect('clientes')
        else:
            error = "Error: El formulario no es válido. Por favor, revise los errores."
            return render(request, 'landing_bd/crear_sociedades.html', {
                'sociedades': SociedadesForm, 'error': error
                })
            

def hoja_sociedad(request, sociedad_id):
    sociedad = get_object_or_404(Sociedades, id=sociedad_id)
    
    if request.method == 'POST':
        form = SociedadesForm(request.POST, instance=sociedad)
        if form.is_valid():
            form.save()
            return redirect('familia')
    else:
        form = SociedadesForm(instance=sociedad)
    
    return render(request, 'landing_bd\hoja_sociedad.html', {'sociedad': sociedad, 'form': form})
            
@login_required           
def eliminar_sociedades(request, sociedad_id):
    sociedades = get_object_or_404(Sociedades, id=sociedad_id)
    if request.method == 'POST':
        sociedades.delete()
        return redirect('familia')

@login_required
def crear_reuniones(request):
    if request.method == 'GET':
        reuniones_form = ReunionesForm()
        return render(request, 'landing_bd/crear_reunion.html', {'reuniones_form': reuniones_form})
    elif request.method == 'POST':
        reuniones_form = ReunionesForm(request.POST, request.FILES)
        if reuniones_form.is_valid():
            reuniones_form.save()
            return redirect('reuniones')
        else:
            error = "Error: El formulario no es válido. Por favor, revise los errores."
            return render(request, 'landing_bd/crear_reunion.html', {'reuniones_form': reuniones_form, 'error': error})

@login_required           
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

@login_required
def eliminar_reunion(request, reunion_id):
    reunion = get_object_or_404(Reuniones, id=reunion_id)
    if request.method == 'POST':
        reunion.delete()
        return redirect('reuniones')

@login_required
def eliminar_familia(request, familia_id):
    familia = get_object_or_404(Familia, id=familia_id)
    if request.method == 'POST':
        familia.delete()
        return redirect('familia')
    
@login_required
def buscar_clientes(request):
    query = request.GET.get('buscar1')
    if query:
        clientes = Cliente.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))
    else:
        clientes = Cliente.objects.annotate(nombre_normalizado=Lower('nombre')).order_by('nombre_normalizado')
    
    return render(request, 'landing_bd/clientes.html', {'clientes': clientes})

@login_required
def buscar_familias(request):
    query = request.GET.get('buscar1')
    if query:
        familia = Familia.objects.filter(Q(nombre__icontains=query))
    else:
        familia = Familia.objects.annotate(nombre_normalizado=Lower('nombre')).order_by('nombre_normalizado')
    
    return render(request, 'landing_bd/familias.html', {'familia': familia})


@login_required
def buscar_reuniones(request):
    query = request.GET.get('buscar1')
    if query:
        reuniones = Reuniones.objects.filter(cliente__nombre__icontains=query)
    else:
        reuniones = Reuniones.objects.order_by('fecha')
    
    return render(request, 'landing_bd/reuniones.html', {'reuniones': reuniones})

from django.shortcuts import render, get_object_or_404

@login_required
def detalles_cliente(request, cliente_id):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        form = ClienteForm(instance=cliente)
        return render(request, 'landing_bd/hoja_cliente.html', {'cliente': cliente, 'form' : form})
    
    else:
        cliente = get_object_or_404(Cliente, id=cliente_id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        else:
            error = 'El formulario no es válido, por favor intente de nuevo'
            return render(request, 'landing_bd/hoja_cliente.html', {'cliente': cliente, 'form': form, 'error': error})

import os

@login_required
def detalles_reuniones(request, reunion_id):
    if request.method == 'GET':
        reunion = get_object_or_404(Reuniones, pk=reunion_id)
        form = ReunionesForm(instance=reunion)
        return render(request, 'landing_bd/reuniones_detail.html', {'reunion': reunion, 'form' : form})
    
    else:
        reunion = get_object_or_404(Reuniones, pk=reunion_id)
        form = ReunionesForm(request.POST, request.FILES, instance=reunion)
        if form.is_valid():
            print(request.FILES)
            if 'archivo' in request.FILES:
                archivo = request.FILES['archivo']
                print(archivo)
            form.save(f"{reunion.id}_{archivo.name}")
            return redirect('reuniones')
            
        else:
            error = 'El formulario no es válido, por favor intente de nuevo'
            return render(request, 'landing_bd/reuniones_detail.html', {'cliente': reunion, 'form': form, 'error': error})

@login_required
def detalles_familia(request, familia_id):
    if request.method == 'GET':
        familia = get_object_or_404(Familia, id=familia_id)
        sociedades = familia.sociedades_familia.all()
        form = FamiliaForm(instance=familia)
        return render(request, 'landing_bd/hoja_familia.html', {'familia': familia, 'sociedades': sociedades,'form' : form})
    
    else:
        familia = get_object_or_404(Familia, id=familia_id)
        form = FamiliaForm(request.POST, instance=familia)
        if form.is_valid():
            form.save()
            return redirect('familia')
        else:
            error = 'El formulario no es válido, por favor intente de nuevo'
            return render(request, 'landing_bd/hoja_familia.html', {'familia': familia, 'form': form, 'error': error})
        
from .resources import ClienteResource, ReunionesResource

def exportar_clientes(request):
    cliente_resource = ClienteResource()
    dataset = cliente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
    return response

def exportar_reuniones(request):
    reuniones_resource = ReunionesResource()
    dataset = reuniones_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reuniones.csv"'
    return response

from tablib import Dataset
def importar_cliente(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = ClienteResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        
        elif file_format == 'XLSX':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xlsx')
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            employee_resource.import_data(dataset, dry_run=False)
            return redirect('clientes')
        
        else:
            errors = result.row_errors
            print(f'hubo un error {errors}')

    return render(request, 'landing_bd/importar_csv.html')    
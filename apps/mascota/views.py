from django.shortcuts import render,redirect
from django.http import HttpResponse
# from . import forms
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
import pdb

def index(request):
	# return HttpResponse("este es el index de mascota") 
	return render(request,'mascota/index.html') 

def mascota_view(request):
	form = MascotaForm()
	return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_crear(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:index')
	else:
		form = MascotaForm()
	return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_listar(request):
	all_mascota = Mascota.objects.all().order_by('id')
	context = {
		'mascotas':all_mascota

	}
	return render(request, 'mascota/mascota_list.html', context)

def mascota_editar(request,id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance= mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_eliminar(request,id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_eliminar.html',{'mascota':mascota})




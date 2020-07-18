from django.shortcuts import render
from django.http import HttpResponse

def index_adopcion(request):
	# return HttpResponse("Este es el index de adopcion")
	return render(request, 'adopcion/index.html')
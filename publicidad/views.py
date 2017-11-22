from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'publicidad/index.html')

def hotel(request):
	return render(request, 'publicidad/hoteles.html')

def bodega(request):
	return render(request, 'publicidad/bodegas.html')

def entretenimiento(request):
	return render(request, 'publicidad/entretenimiento.html')

def santuario(request):
	return render(request, 'publicidad/santuarios.html')

def restaurante(request):
	return render(request, 'publicidad/restaurante.html')

def supermercado(request):
	return render(request, 'publicidad/supermercado.html')	

def publico(request):
	return render(request,'publicidad/publicos.html')

def surtidor(request):
	return render(request, 'publicidad/surtidor.html')

def bar(request):
	return render(request, 'publicidad/baresYdiscotecas.html')

def plazaTtefarina(request):
	return render(request, 'publicidad/sector_publico/plazaTteFarina.html')

def petropar(request):
	return render(request, 'publicidad/surtidor/petropar.html')

def brothers(request):
	return render(request, 'publicidad/baresYdiscotecas/brothers.html')
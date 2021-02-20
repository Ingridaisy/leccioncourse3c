from django.shortcuts import render, HttpResponse


def home(request):
  return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")


from django.shortcuts import render

# Create your views here.

def acerca(request):
  return render(request,'acerca de.html')

def base(request):
  return render(request,'base.html')

def contacto(request):
  return render(request,'contacto.html')

def portafolio(request):
  return render(request,'portafolio.html')
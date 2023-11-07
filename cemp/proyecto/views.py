from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'proyecto/home.html')

def adopcion(request):
    return render(request,'proyecto/adopcion.html')
def informacion(request):
    return render(request,'proyecto/informacion.html')
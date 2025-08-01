from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Página de inicio")

def contacto(request):
    return HttpResponse("Página de contacto")

def nosotros(request):
    return HttpResponse("Sobre nosotros")
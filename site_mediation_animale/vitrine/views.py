from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil du site de médiation animale.")

def about(request):
    return HttpResponse("À propos de Ludivine et de son parcours.")

def services(request):
    return HttpResponse("Les services proposés : ateliers, médiation animale, etc.")

def gallery(request):
    return HttpResponse("Galerie de photos des activités de médiation animale.")

def contact(request):
    return HttpResponse("Page de contact pour joindre Ludivine.")

from django.shortcuts import render

# Vue pour la page d'accueil
def home(request):
    return render(request, 'vitrine/home.html')

# Vue pour la page "À propos"
def about(request):
    return render(request, 'vitrine/about.html')

# Vue pour la page des services
def services(request):
    return render(request, 'vitrine/services.html')

# Vue pour la galerie
def gallery(request):
    return render(request, 'vitrine/gallery.html')

# Vue pour la page de contact
def contact(request):
    return render(request, 'vitrine/contact.html')

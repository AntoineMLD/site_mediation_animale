from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('about/', views.about, name='about'),  # Page À propos
    path('services/', views.services, name='services'),  # Page Services
    path('gallery/', views.gallery, name='gallery'),  # Page Galerie
    path('contact/', views.contact, name='contact'),  # Page Contact
]
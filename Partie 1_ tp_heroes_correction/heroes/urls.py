
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hero/<int:id>/', views.detail, name='detail'),
    path('ajouter/', views.ajouter_hero, name='ajouter_hero'),
]
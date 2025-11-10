from django.db import models
from django.contrib.auth.models import AbstractUser

class SuperHero(models.Model):
    nom = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    puissance = models.IntegerField()
    actif = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nom} ({self.alias})"
    
class Pouvoir(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    heroes = models.ManyToManyField(SuperHero, related_name='pouvoirs')

    def __str__(self):
        return self.nom

class HeroUser(AbstractUser):
    favorite_hero = models.ForeignKey(
        'SuperHero',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='fans'
    )

    def __str__(self):
        return f"{self.username} (Fan de {self.favorite_hero or 'aucun héros'})"

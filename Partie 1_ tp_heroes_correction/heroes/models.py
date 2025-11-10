from django.db import models

class SuperHero(models.Model):
    nom = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    puissance = models.IntegerField()
    actif = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nom} ({self.alias})"

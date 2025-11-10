from django import forms
from .models import SuperHero

class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHero
        fields = ['nom', 'alias', 'puissance', 'actif']

from django.test import TestCase
from django.urls import reverse
from .models import SuperHero

class SuperHeroModelTest(TestCase):
    def setUp(self):
        # Création d'un héros pour les tests
        SuperHero.objects.create(
            nom="Bruce Wayne", alias="Batman", puissance=90, actif=True
        )

    def test_str_affiche_nom_et_alias(self):
        hero = SuperHero.objects.get(alias="Batman")
        self.assertEqual(str(hero), "Bruce Wayne (Batman)")


class SuperHeroViewTest(TestCase):
    def setUp(self):
        # Préparer les données de test
        SuperHero.objects.create(
            nom="Clark Kent", alias="Superman", puissance=100, actif=True
        )

    def test_page_index_affiche_heroes(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)  # la page existe
        self.assertContains(response, "Superman")     # le nom du héros apparaît


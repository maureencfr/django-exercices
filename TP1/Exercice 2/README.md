# TP Django : Gestion des Super Héros

## Exercice 2

**Remarque :** Cet exercice est la suite de l’Exercice 1 et permet de consolider vos connaissances sur Django, le modèle MVT et l’ORM.

## Étape 8 : Créer un formulaire pour ajouter des Super Héros

1. Créer un fichier `forms.py` dans ton app `heroes`
2. Définir un formulaire basé sur le modèle `SuperHero` (ModelForm)
3. Créer une vue `ajouter_hero()` pour afficher et traiter le formulaire
4. Créer le template `ajouter.html` contenant le formulaire
5. Ajouter une route `/ajouter/` dans `urls.py`
6. Tester l’ajout d’un héros et vérifier son affichage dans la liste

---

## Étape 9 : Tester son application

1. Créer un fichier `tests.py` dans l’application `heroes`
2. Écrire une classe de tests pour vérifier que :
   - La méthode `__str__` du modèle retourne bien le bon format
   - La page principale (`index`) renvoie un code 200 et affiche les héros
3. Lancer les tests avec :

```bash
python manage.py test
```
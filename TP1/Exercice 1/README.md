# TP Django : Gestion des Super Héros

## Exercice 1 

## Objectifs

- Comprendre la structure MVT (Model – View – Template) de Django.
- Manipuler l’ORM de Django pour créer, lire, modifier et supprimer des données.
- Apprendre à relier une vue et un template via une route (routage explicite).
- Créer une mini-application complète sans passer par l’admin auto-généré.

---

## Étape 0 : Pré-requis
Avant de commencer, assurez-vous que votre environnement de travail est correctement configuré :

- Python installé : `python --version` - `python3 --version`
- Django installé : `python -m django --version` si rien ->  `pip install django`
- Requests installé : `pip install requests`

**Si vous ne parvenez pas à créer un projet, clonez ce dépôt : Pour vous faire gagner du temps, les étapes**
- *Création du projet Django*
-  *Création et configuration de l'application Django* 
**ont déjà été réalisées.**

### Création du projet Django

```bash
django-admin startproject tp_heroes

# OU pour les environnements de la fac :
python -m django startproject tp_heroes

cd tp_heroes
```

### Création et configuration de l'application Django

```bash
python manage.py startapp heroes
```

#### Ajouter l’application dans `settings.py`

Dans le fichier `settings.py`, ajouter `heroes` à la liste `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'heroes',  # ajout de l'application
]
```

#### Préparer la base de données

```bash
python manage.py migrate
```

#### Créer un superutilisateur

```bash
python python manage.py createsuperuser
```

#### Lancer le serveur de développement

```bash
python manage.py runserver
```
- Ouvrir ensuite le navigateur à l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Étape 1 : Créer le modèle

Créer un modèle `SuperHero` dans le fichier `heroes/models.py` contenant :

- un nom
- un alias
- un niveau de puissance
- un statut actif (booléen)

Appliquer ensuite les migrations pour créer la table correspondante :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Étape 2 : Manipuler les données avec l’ORM

Lancer le shell Django :

```bash
python manage.py shell
```

### Tâches à réaliser 

- Créer quelques héros avec leur nom, alias, puissance et statut
- Lister tous les héros enregistrés
- Filtrer les héros actifs
- Mettre à jour un héros (modifier sa puissance)
- Supprimer un héros

---

## Étape 3 : Créer une vue (View)

Créer une fonction `index(request)` dans `heroes/views.py`.  
Cette vue doit :

- Récupérer tous les super-héros depuis la base
- Envoyer cette liste au template via la fonction `render()`

---

## Étape 4 : Configurer le routage (URL)

1. Créer un fichier `urls.py` dans l’app `heroes`
2. Déclarer une route vide `""` qui appelle la vue `index()`
3. Inclure ces routes dans le fichier principal `tp_heroes/urls.py`

---

## Étape 5 : Créer un template (Template)

1. Créer un dossier `templates/heroes` dans l’app `heroes`
2. À l’intérieur, créer le fichier `index.html`
3. Afficher la liste des super-héros sous forme de tableau HTML :

- nom
- alias
- puissance
- statut actif

* Utiliser une boucle `{% for hero in heroes %}`

---

## Étape 6 : Ajouter une page de détail (bonus)

1. Créer une vue `detail(request, id)` dans `views.py`
2. Afficher les informations détaillées d’un seul héros
3. Créer le template `detail.html`
4. Ajouter une route `hero/<int:id>/` pour accéder à cette page

---

## Étape 7 : Ajouter des fichiers statiques (bonus)

1. Dans l’app `heroes`, créer le dossier :  `heroes/static/heroes/`

2. Créer un fichier CSS simple `style.css` dans ce dossier  
```django
body {
    background-color: #f5f5f5;
    font-family: Arial;
}
h1 {
    color: #2b3a67;
}
```

3. Relier le CSS au template `index.html` en ajoutant au début du fichier :  

```django
{% load static %}
<link rel="stylesheet" href="{% static 'heroes/style.css' %}">
```

4. Ajouter la configuration suivante pour que Django puisse trouver vos fichiers CSS, JS ou images :

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

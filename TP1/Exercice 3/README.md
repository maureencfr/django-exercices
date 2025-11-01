# TP Django : Gestion des Super Héros - Partie Administrateur

## Exercice 2

**Remarque :** Cet exercice est la suite de l’Exercice 2 et permet de découvrir l’interface d’administration Django, qui permet de gérer les objets SuperHero et Pouvoir depuis une interface graphique.

## Objectifs
- Découvrir l’admin auto-généré.
 -Personnaliser l’affichage (list_display), ajouter filtres (list_filter) et recherche (search_fields).
- Créer une action personnalisée sur plusieurs objets.


## Étape 0 : Pré-requis

1. Si tu as déjà fait le TP “MVT & ORM – Super Héros”, reprends le même projet tp_heroes. Sinon, reprend la correction de ce TP pour pouvoir continuer celui-ci !
2. Avoir créé le superuser (disponible dans le premier exercice)

---

## Étape 1 : Ajout d'un nouveau modèle

1. Rends toi dans le fichier `models.py`
2. Écrire un nouveau modèle : Pouvoir. Les pouvoirs doivent contenir un nom de maximum 50 caractères et une description. Les pouvoirs peuvent être associés à plusieurs héros.

*Conseil : n'oubliez pas d'appliquer les migrations*

## Étape 2 : Enregistrer et personnaliser l’admin

Enregistrez les modèles dans l’administrateur
1. Réalisez un admin simple dans un affichage par défaut pour Pouvoir.
2. Réalisez un admin personnalisé pour SuperHero. On veut pouvoir :  
    1. afficher dans la liste les différents champs de SuperHero  
    2. filtrer les super-héros par “actif”  
    3. créer une action groupée de désactivation des héros pour tous les héros sélectionnés

## Étape 3 : Instructions pour tester

1. Lancer le serveur :
`python manage.py runserver`
2. Accéder à l’admin : http://127.0.0.1:8000/admin
3. Se connecter avec le superuser créé.
4. Ajouter quelques SuperHéros et Pouvoirs.
5. Vérifier :  
- la recherche par nom ou alias,
- le filtrage par statut actif,
- l’action “Désactiver les héros sélectionnés”.
6. Observer que les changements apparaissent immédiatement dans l’interface.


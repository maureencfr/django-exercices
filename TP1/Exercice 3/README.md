# TP Django : Gestion des Super Héros - Partie Administrateur

## Exercice 3

**Remarque :** Cet exercice est la suite de l’Exercice 2 et permet de découvrir l’interface d’administration Django, qui permet de gérer les objets SuperHero et Pouvoir depuis une interface graphique.

## Objectifs
- Découvrir l’admin auto-généré.
- Personnaliser l’affichage (list_display), ajouter filtres (list_filter) et recherche (search_fields).
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

## Étape 4 : Bonus

1. Personnaliser l'admin des Pouvoirs afin qu'on puisse voir la description de ce pouvoir dans la liste et qu'on puisse rechercher les pouvoirs par nom.
2. Créer une action permettant de (ré)activer un héros.
3. Ajouter la liste des Pouvoirs de chaque héros dans la liste des SuperHeroes.

## Étape 5 : Bonus Bonus
 Vous êtes rapides ! Intéressons-nous maintenant à l'authentification.

Le modèle User par défaut de Django est très complet, mais parfois il faut le personnaliser pour qu'il corresponde au besoin.
Dans cette extension, tu vas créer un modèle utilisateur personnalisé, qui ajoute un champ favorite_hero pour lier chaque utilisateur à son héros préféré.
Pas de panique ! Tout est détaillé dans les étapes ci-dessous.

1. Créer le modèle HeroUser. Ce modèle devra étendre la classe AbstractUser(elle fournit les bases du User standard) et contenir le champ ```favourite_hero``` qui lie le HeroUser à un SuperHero.
Conseil : renseigne toi sur le ```on_delete```, cela pourrait t'être utile !
**Avant de faire ta migration**
2. Mettre à jour la configuration. Dans ```settings.py```, il faut indiquer ton modèle à utiliser
   ```AUTH_USER_MODEL = "heroes.HeroUser"```
**Si tu migres avant, Django créera la table auth_user standard**
3. Créer et appliquer les migrations
4. Enregistrer le modèle dans l’admin. Dans ton fichier ```admin.py```, crée la classe HeroUserAdmin qui étend UserAdmin(classe d’administration du modèle utilisateur standard). Assure toi d'afficher le héro préféré de l'utilisateur en plus des champs déjà inclus !

### Pour tester
1. Lance ton serveur (python manage.py runserver)
2. Connecte-toi à l’admin (http://127.0.0.1:8000/admin)
3. Ouvre la section Hero Users
4. Crée un nouvel utilisateur et choisis un héros préféré. Tu devrais voir la colonne “Héros préféré” dans la liste.


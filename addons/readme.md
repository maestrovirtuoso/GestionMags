README - Module Gestion de Boutique (gestion_p)
Description
Ce module Odoo permet de gérer une boutique en ligne avec les fonctionnalités suivantes :

Gestion des catégories de produits

Gestion des produits avec images et prix

Gestion des utilisateurs (clients/comptes)

Fonctionnalités Clés
Catégories
Création de catégories (ex: Électronique, Vêtements)

Affichage des produits associés via des tags

Glisser-déposer pour réorganiser les catégories

Produits
Fiche produit détaillée avec onglets

Upload d'image produit

Prix avec format monétaire

Filtre de recherche "Prix > 100"

Utilisateurs
Profil utilisateur complet (nom, email, mot de passe)

Champ mot de passe sécurisé

Mise en évidence des utilisateurs sans email (en rouge)

Installation
Placer le dossier gestion_p dans le répertoire addons d'Odoo

Actualiser la liste des apps dans Odoo (Mode Développeur)

Rechercher "Boutique" dans les apps et installer

Utilisation
Accéder aux fonctionnalités
Catégories :

Menu → Boutique → Catégories

Bouton "Retour" dans les formulaires

Produits :

Vue Kanban/Liste/Formulaire

Recherche par catégorie ou nom

Utilisateurs :

Liste filtrable par email ou username

Formulaire avec validation de date de naissance

**Notes Techniques
Modèles
gestionp_category : Catégories hiérarchiques

gestionp_product : Produits avec relation Many2one vers les catégories

gestionp_user : Utilisateurs avec champs de profil

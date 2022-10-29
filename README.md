# Conception mini interface gestion stock d'un restaurant fictif

Création d'une interface pour un restaurant fictif en Python avec une BDD (avec sqlite3)
Gestion des clients, de l'inventaire et des recettes.

# Explications

database.db sert d'intermédiaire pour intéragir avec les tables de la BD

tablesql.py sert à importer dans l'application les tables et les insertions de la BD

interface.py est l'application exécutable et son code source est directement visible 
depuis un IDE(nous avons utilisé Thonny avec Python 3.7.9 bundled)

La base de données est déjà pré-remplie avec des valeurs
Vous pouvez modifier la base à votre guise sans fermer la fenetre d'interface.
Des boutons retour sont prévus et la réalisation d'une fonction ne coupe pas la fenêtre.
A chaque relance du programme, la base initiale sera relancée.
Le bouton Terminer ferme le programme.

- Pour utiliser l'appication, lancez interface.py avec Thonny
- Cliquez sur la flèche verte (Run) ou F5
- L'interface graphique apparait avec 9 boutons
- Vous pouvez intéragir avec les différentes fonctions grâce aux boutons
- Par exemple, en cliquant sur nouveau client, vous pouvez ajouter à la BD un client en entrant
son nom et prénom, puis cliquer sur Ajouter, un retour au menu principal s'effectura
et le client sera dans la DB
- S'il y a un problème dans le nom, afficher les clients et double cliquez dessus pour modifier
- Supprimer un client supprime un client en entrant son nom de famille
- Supprimer une réservation avec son id client et la date de la réservation
- Afficher réservation pour visualiser les réservation et double cliquer pour modifier
- idem pour afficher le stock
- bouton pour afficher le client qui a le plus dépensé

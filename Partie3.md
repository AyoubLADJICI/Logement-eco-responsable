# TP IoT - Logement Éco-Responsable

## 🌐 HTML/CSS/Javascript
Dans cette partie, j'ai développé mon site avec une page accueil et 4 autres onglets présentant la consommation (électricité, eau, gaz et Internet), l'état des différents capteurs/actionneurs, les économies réalisées par rapport au mois précédent, la configuration permettant d'ajouter un nouveau logement, de nouveaux capteurs/actionneurs.

La page d'accueil est accessible sur : http://127.0.0.1:8000/
📑Les sections ont été organisés de la façon suivante:
- Une barre de navigation fixe en haut de la page, avec le logo centré et les onglets de navigation à gauche et à droite.
- Intégration d'un widget météo adaptatif provenant de ce **[`site`](https://weatherwidget.org/fr/)** et affiche les prévisions météo en temps réel de notre localisation actuelle et s'adapte automatiquement à l'écran. Cela concerne les ```lignes 34 à 35```. 
- Une section d'accueil avec un message de bienvenue et une courte description, placée dans une bloc vert centré.
- Une section qui met en avant les fonctionnalités principales de l'application.
- Une section qui est dédiée aux statistiques dynamiques récupérées depuis le serveur sur le nombre de logements, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées.
- Une section permettant aux utilisateurs de contacter le propriétaire du site. Toutefois, il n'a pas été configuré pour envoyer réellement un message.

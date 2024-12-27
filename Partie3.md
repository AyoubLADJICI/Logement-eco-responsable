# TP IoT - Logement Éco-Responsable

## 🌐 HTML/CSS/Javascript
Dans cette partie, j'ai développé mon site avec une page accueil et 4 autres onglets présentant la consommation (électricité, eau, gaz et Internet), l'état des différents capteurs/actionneurs, les économies réalisées par rapport au mois précédent, la configuration permettant d'ajouter un nouveau logement, de nouveaux capteurs/actionneurs.

La page d'accueil est accessible sur : http://127.0.0.1:8000/
📑Les sections ont été organisés de la façon suivante:
- Une barre de navigation fixe en haut de la page, avec le logo centré et les onglets de navigation à gauche et à droite.
- Intégration d'un widget météo adaptatif provenant de ce **[`site`](https://weatherwidget.org/fr/)** et affiche les prévisions météo en temps réel de notre localisation actuelle et s'adapte automatiquement à l'écran. 
- Le style a été entièrement généré par ChatGPT, en répondant à mes prompts concernant le design et l'alignement des éléments

J'ai utilisé Bootstrap 5 pour la mise en page réactive et HTML/CSS pour la structure et le style.

📑 Organisation des Sections :
Barre de Navigation :

Une barre de navigation fixe en haut de la page, avec le logo centré et les onglets de navigation à gauche et à droite.
Le style a été entièrement généré par ChatGPT, en répondant à mes prompts concernant le design et l'alignement des éléments.
Lignes concernées : 1-30 dans le fichier index.css.
Widget Météo :

Intégration d'un widget météo adaptatif provenant de WeatherWidget.org.
Le widget affiche les prévisions météo en temps réel et s'adapte automatiquement à l'écran.
Lignes concernées : 31-40 dans le fichier index.css et ajout du script au fichier index.html.
Section d'Accueil :

Une section d'accueil avec un titre principal et une courte description, placée dans une boîte verte au centre.
Design réalisé par ChatGPT avec une approche responsive.
Lignes concernées : 41-60 dans le fichier index.css.
3.2 Nos Fonctionnalités
Dans cette section, j'ai mis en avant les trois fonctionnalités principales de l'application :

Suivi de la Consommation
Gestion des Capteurs
Économies Réalisées
Ces fonctionnalités sont présentées sous forme de cartes interactives avec des effets de survol.

📑 Prompt ChatGPT :

"Peux-tu créer une section avec trois cartes interactives, chacune représentant une fonctionnalité clé, et ajouter des effets CSS au survol ?"

Lignes concernées : 61-90 dans le fichier index.css.

3.3 Nos Statistiques
Une section dédiée aux statistiques dynamiques récupérées depuis le serveur Python.

Données Affichées :

Nombre de logements
Types de capteurs/actionneurs
Capteurs/actionneurs actifs
Mesures enregistrées
Prompt ChatGPT :

"Crée une section statistique avec quatre cartes affichant des valeurs dynamiques récupérées via JavaScript et propose un design interactif."

Lignes concernées : 91-110 dans le fichier index.css.

Fonction JavaScript dans le fichier index.html, lignes 220-230.

3.4 Contactez-nous
Une section permettant aux utilisateurs de contacter l'équipe via un formulaire simple.

📑 Détails :
Bloc gauche : Informations de contact (email, téléphone, LinkedIn).

Bloc droit : Formulaire avec champs obligatoires pour le prénom, nom, email et message.

📑 Prompt ChatGPT :

"Crée une section contact avec deux colonnes, une pour les informations de contact et une autre pour un formulaire stylisé avec validation."

Lignes concernées : 111-150 dans le fichier index.css.

3.5 Pied de Page
Le pied de page a été harmonisé avec la barre de navigation :

Couleur identique (#2c3e50) pour maintenir une cohérence visuelle.

Texte centré et liens interactifs.

📑 Prompt ChatGPT :

"Peux-tu styliser le pied de page avec la même couleur que la barre de navigation et centrer le texte ?"

Lignes concernées : 151-160 dans le fichier index.css.

3.6 Scripts JavaScript
Récupération des statistiques dynamiques :

JavaScript est utilisé pour récupérer les statistiques via une API Flask sur /api/statistics.
Les données sont affichées dynamiquement dans la section des statistiques.
📑 Prompt ChatGPT :

"Ajoute un script JavaScript pour récupérer des données statistiques via une API Flask et les afficher dynamiquement sur la page."

Lignes concernées : 220-230 dans le fichier index.html.


# TP IoT - Logement Éco-Responsable

## 🌐 HTML/CSS/Javascript
Dans cette partie, j'ai développé mon site avec une page accueil et 4 autres onglets présentant la consommation (électricité, eau, gaz et Internet), l'état des différents capteurs/actionneurs, les économies réalisées par rapport au mois précédent, la configuration permettant d'ajouter un nouveau logement, de nouveaux capteurs/actionneurs.

Dans le fichier **🐍[`serveur.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/serveur.py)**, les lignes 340 à 363 définissent plusieurs routes dans notre application, chacune renvoyant une page HTML lorsqu'on essaie d'y accéder, cela est possible grâce à notre moteur de templates Jinja2. J'ai utilisé le prompt suivant sur ChatGPT : ```Peux-tu m'écrire des fonctions Python permettant de retourner des pages HTML pour chaque onglet de notre application ? en utilisant le moteur Jinja2 stp```

👉 La page d'accueil est accessible sur : http://127.0.0.1:8000/

📑Les sections ont été organisés de la façon suivante:
- Une barre de navigation fixe en haut de la page, avec le logo centré et les onglets de navigation à gauche et à droite.
- Intégration d'un widget météo adaptatif provenant de ce **[`site`](https://weatherwidget.org/fr/)** et affiche les prévisions météo en temps réel de notre localisation actuelle et s'adapte automatiquement à l'écran. Cela concerne les ```lignes 34 à 35``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**. 
- Une section d'accueil avec un message de bienvenue et une courte description, placée dans une bloc vert centré.
- Une section qui met en avant les fonctionnalités principales de l'application.
- Une section qui est dédiée aux statistiques dynamiques récupérées depuis le serveur sur le nombre de logements, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées.
- Une section permettant aux utilisateurs de contacter le propriétaire du site. Toutefois, il n'a pas été configuré pour envoyer réellement un message.

L'intégralité du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)** et **[`accueil.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/accueil.css)** ont été écrits à l'aide de plusieurs prompts sur ChatGPT 🤖.

1️⃣ Barre de navigation et pied de page :
- "Peux-tu créer une barre de navigation avec notre logo (celui que je t'ai envoyé précédemment) centré et des onglets à gauche (Accueil, Consommation) et à droite (État des capteurs, Économies, Configuration) dans le fichier accueil.html ? Et aussi si tu peux aussi ajouter un pied de page de la même couleur que la barre de navigation" Cela concerne les ```lignes 12 à 32``` et ```158 à 160``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)** .

2️⃣ Widget météo :
- "J'ai récupéré ce code html (..) qui permet d'afficher les données météo en temps réel de notre localisation actuelle, comment je peux l'intégrer dans mon code ?" Cela concerne les ```lignes 34 à 35```` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

3️⃣ Section d'accueil :
- "Peux-tu ajouter une section d'accueil avec un texte de bienvenue centré dans un bloc vert s'il te plaît ?"  Cela concerne les ```lignes 38 à 43``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

4️⃣ Section fonctionnalités :
- "Maintenant, peux-tu ajouter des blocs pour présenter les fonctionnalités principales de notre application ?" Cela concerne les ```lignes 46 à 75``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)** + "Peux-tu écrire une fonction Python qui récupère les statistiques tels que le nombre de logement, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées dans ma base de donnée pour pouvoir les afficher sur ma page HTML ?" Cela concerne les ```lignes 365 à 378``` du fichier **🐍[`serveur.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/serveur.py)**.

5️⃣ Section statistiques :
- "Peux-tu créer une section pour afficher des statistiques comme le nombre de logements, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées avec des couleurs distinctes ?"  Cela concerne les ```lignes 77 à 108``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

6️⃣ Section contact :
- "Pour le fun, peux-tu créer une section contact avec un formulaire et une boîte d'informations alignée en t'inspirant d'autres sites comme celui du messervices.etudiant.gouv.fr ? et rajoute une politique de confidentialité un peu marrante qu'on pourra écrire dans le fichier **[`condidentialite.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/consommation.html)**   Cela concerne les ```lignes 111 à 155``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

7️⃣ CSS général :
- "Pour finaliser notre page, ajoute du style CSS pour chaque section avec des effets de survol et peux-tu essayer de le rendre responsive ?" Cela concerne l'intégralité du fichier **[`accueil.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/accueil.css)**.


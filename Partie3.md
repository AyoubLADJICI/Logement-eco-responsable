# TP IoT - Logement Éco-Responsable

## 🌐 HTML/CSS/Javascript
Dans cette partie, j'ai développé mon site avec une page d'accueil et 4 autres onglets présentant la consommation (électricité, eau, gaz et Internet), l'état des différents capteurs/actionneurs, les économies réalisées par rapport au mois précédent, la configuration permettant d'ajouter un nouveau logement, de nouveaux capteurs/actionneurs.

Dans le fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**, les lignes 340 à 363 définissent plusieurs routes dans notre application, chacune renvoyant une page HTML lorsqu'on essaie d'y accéder, cela est possible grâce à notre moteur de templates Jinja2. J'ai utilisé le prompt suivant sur ChatGPT : ```Peux-tu m'écrire des fonctions Python permettant de retourner des pages HTML pour chaque onglet de notre application ? en utilisant le moteur Jinja2 s'il te plaît```

👉 La page d'accueil est accessible sur : http://127.0.0.1:8000/

📝 Structure de la page Accueil :
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
- "Maintenant, peux-tu ajouter des blocs pour présenter les fonctionnalités principales de notre application ?" Cela concerne les ```lignes 46 à 75``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)** + "Peux-tu écrire une fonction Python qui récupère les statistiques tels que le nombre de logement, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées dans ma base de donnée pour pouvoir les afficher sur ma page HTML ?" Cela concerne les ```lignes 366 à 379``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.

5️⃣ Section statistiques :
- "Peux-tu créer une section pour afficher des statistiques comme le nombre de logements, de types de capteurs/actionneurs, de capteurs/actionneurs installés et de mesures enregistrées avec des couleurs distinctes ?"  Cela concerne les ```lignes 77 à 108``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

6️⃣ Section contact :
- "Pour le fun, peux-tu créer une section contact avec un formulaire et une boîte d'informations alignée en t'inspirant d'autres sites comme celui du messervices.etudiant.gouv.fr ? et rajoute une politique de confidentialité un peu marrante qu'on pourra écrire dans le fichier **[`condidentialite.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/consommation.html)**   Cela concerne les ```lignes 111 à 155``` du fichier **[`accueil.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/accueil.html)**.

7️⃣ CSS général :
- "Pour finaliser notre page, ajoute du style CSS pour chaque section avec des effets de survol et peux-tu essayer de le rendre responsive ?" Cela concerne l'intégralité du fichier **[`accueil.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/accueil.css)**.

👉 L'onglet Consommation est accessible sur : http://127.0.0.1:8000/consommation

📝 Structure de la page Consommation :
- Une barre de navigation fixe en haut de la page avec le logo centré, des onglets à gauche (Accueil, Consommation) et à droite (État des capteurs, Économies, Configuration)
- Nous avons un sélecteur permettant de choisir un logement pour afficher ses données spécifiques
- 3 Boutons : Graphiques en Temps Réel (qui affiche des courbes de consommation de chaque type), Graphique en Camembert des montants par type de fatcure sur 7 jours, Graphique en Camembert des factures depuis le début (renvoie vers le le lien suivant : ```http://127.0.0.1:8000/factures/chart``` en ouvrant un nouvel onglet)

L'intégralité du fichier **[`consommation.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/consommation.html)** et **[`consommation.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/consommation.css)** ont été écrits à l'aide de plusieurs prompts sur ChatGPT.

1️⃣ Python: "Peux-tu écrire une fonction Python pour récupérer la liste des logements de ma base, avec leur ID et adresse comme ça je pourrai les afficher sur mon site après ?" Cela concerne les ```lignes 381 à 384``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.
"Peux-tu écrire une fonction Python pour récupérer les données de consommation des 7 derniers jours, avec une option pour filtrer les données en fonction de l'id du logement ?" Cela concerne les ```lignes 386 à 408``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.

2️⃣ HTML: "Peux-tu créer une page HTML en essayant de garder le même style que pour la page d'accueil mais ici je veux que tu ajoutes un sélecteur de logement, des graphiques interactifs (courbes et camembert) sur les valeurs de consommation depuis ma base de données pour chaque type (Electricite, Eau, Gaz, Internet) et également un bouton qui renvoie le précédent site que j'avais crée ```http://127.0.0.1:8000/factures/chart``` dans un nouvel onglet ?" Cela concerne l'intégralité du fichier **[`consommation.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/consommation.html)**.

3️⃣ CSS : "Peux-tu ajouter du style CSS pour rendre cette page responsive en gardant le même style que la page d'Accueil ?" cela concerne l'intégralité du fichier **[`consommation.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/consommation.css)**.

👉 L'onglet État des capteurs est accessible sur : http://127.0.0.1:8000/etat_capteurs

📝 Structure de la page État des capteurs :
- Une barre de navigation fixe en haut de la page avec le logo centré, des onglets à gauche (Accueil, Consommation) et à droite (État des capteurs, Économies, Configuration).
- Une liste déroulante permettant de choisir un logement spécifique pour afficher ses capteurs et actionneurs associés.
- Une fois le logement sélectionné, les différentes pièces sont affichées avec chacune contenant les capteurs/actionneurs associés.
- Chaque capteur/actionneur dispose d'un bouton ON/OFF permettant de basculer son état directement.

L'intégralité du fichier **[`etat_capteurs.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/etat_capteurs.html)** et **[`etat_capteurs.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/etat_capteurs.css)** ont été écrits à l'aide de plusieurs prompts sur ChatGPT.

1️⃣ Python: "Peux-tu écrire une fonction Python pour récupérer les pièces et leurs capteurs associés en fonction de l'ID d'un logement ? Chaque capteur doit afficher son ID, son nom, sa référence commerciale, son port communication et son état." Cela concerne les ```lignes 410 à 435``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.
"Peux-tu écrire une fonction Python pour qu'ensuite sur le site je peux piloter l'état de mon capteur et mettre à jour cette information dans ma base de données ?" Cela concerne les ```lignes 437 à 454``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.

2️⃣ HTML: "Peux-tu créer une page HTML gardant le même style que les précédents onglets et permettant de sélectionner un logement depuis une liste déroulante et d'afficher les pièces associées avec leurs capteurs ? Chaque capteur doit afficher son état ON/OFF avec un bouton Activer/Désactiver pour le basculer. Et rajoute une fonctionnalité qui permet de conserver l'état de ma page lorsque je le rafrachis ça veut dire que si le capteur de mon salon est activer alors le bouton pour désactiver ne se réinitialise pas quand je clique sur F5" Cela concerne l'intégralité du fichier **[`etat_capteurs.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/etat_capteurs.html)**.

3️⃣ CSS : "Peux-tu ajouter du style CSS pour bien organiser les différents blocs, les boutons ON/OFF et rendre la page responsive tout en conservant le style général de la page d'accueil ?" Cela concerne l'intégralité du fichier **[`etat_capteurs.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/etat_capteurs.css)**.

👉 L'onglet Économies est accessible sur : http://127.0.0.1:8000/economies

📝 Structure de la page Économies :

- Un menu déroulant permettant de choisir un logement spécifique afin d'afficher les données correspondantes.
- Un graphique à barres affichant l'évolution du montant payé par mois pour chaque type de consommation
- 4 tableaux séparés affichent les détails des économies pour chaque type de consommation : électricité, eau, gaz et Internet

L'intégralité du fichier **[`economies.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/economies.html)** et **[`economies.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/economies.css)** ont été écrits à l'aide de plusieurs prompts sur ChatGPT.

1️⃣ Python: "Peux-tu écrire une fonction Python pour récupérer les montants payé chaque mois et par type de facture afin de pouvoir établir le pourcentage d'économie par rapport au mois précédent." Cela concerne les ```lignes 456 à 486``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.

2️⃣ HTML: "Peux-tu ajouter un sélecteur permettant de choisir un logement et afficher les montants payés chaque mois par type de facture dans un graphique à barre ? Puis l'afficher avec 4 tableaux distincts et indiquer le pourcentage d'économie par rapport au mois précédent" Cela concerne l'intégralité du fichier **[`economies.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/economies.html)**. 

3️⃣ CSS : "Peux-tu rajouter un fichier css pour le rendre beau à voir et bien évidemment responsive comme les précédents onglets ?" Cela concerne l'intégralité du fichier **[`economies.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/economies.css)**.

👉 L'onglet Configuration est accessible sur : http://127.0.0.1:8000/configuration

📝 Structure de la page Configuration :
- Une barre de navigation fixe en haut de la page avec le logo centré, des onglets à gauche (Accueil, Consommation) et à droite (État des capteurs, Économies, Configuration).
- Première section permettant une gestion des logements existants avec la possibilité de les modifier, de les supprimer ou même d'en ajouter un nouveau en remplissant un formulaire.
- Deuxième section similaire à la première mais qui concerne les pièces d'un logement.
- Dernière section permettant d'ajouter un capteur dans une pièce d'un logement.

1️⃣ Python: "Peux-tu écrire des fonctions Python permettant d'ajouter, modifier et supprimer les logements, pièces, capteurs/actionneurs en respectant bien les classes que j'ai défini au tout début ?" Cela concerne les ```lignes 489 à 602``` du fichier **🐍[`main.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/main.py)**.

2️⃣ HTML: "Peux-tu créer une section HTML pour afficher une liste de logements avec des boutons pour ajouter, modifier en remplissant un formulaire dans une boîte de dialogue et supprimer chaque logement ? Fais aussi la même pour les pièces de chaque logement et rajoute une dernière section pour ajouter des capteurs/actionneurs"  Cela concerne l'intégralité du fichier **[`configuration.html`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/templates/configuration.html)**. 

3️⃣ CSS : "Peux-tu rajouter un fichier css pour le rendre beau à voir et bien évidemment responsive comme les précédents onglets ?" Cela concerne l'intégralité du fichier **[`configuration.css`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/static/css/configuration.css)**.





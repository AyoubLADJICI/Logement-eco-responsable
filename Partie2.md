# TP IoT - Logement Éco-Responsable

## 🌐 Partie 2 : Serveur RESTful
### 2.1 Exercice 1 : remplissage de la base de données
Dans cette partie, j'ai développé un serveur RESTful pour interagir avec la base de données logement.db créée dans la Partie 1.

J'ai utilisé FastAPI pour créer des API RESTful en raison de sa simplicité et de sa documentation interactive.
J'ai utilisé SQLModel, une bibliothèque Python qui a d'ailleurs été développée par le créateur de FastAPI, et qui manipule le modèle SQLite.
J'ai suivi ce **[`tutoriel`](https://fastapi.tiangolo.com/tutorial/sql-databases/)** qui couvre :
- La définition des modèles SQLModel sous forme de classes Python.
- La création d'un moteur SQL pour la connexion à la base de données ```logement.db```.
- La création des tables de notre base de données en s'appuyant sur les modèles qu'on a crée précédemment. 
- Le développement de route (Create, Read, Update, Delete) pour chaque table.
- Chaque table dispose des opérations suivantes : GET, POST, DELETE

💻 Nous pouvons lancer l'application en tapant la commande suivante sur le terminal : ```fastapi dev serveur.py```
- 🚀 Serveur accessible sur : http://127.0.0.1:8000/
- 📚 Documentation interactive Swagger : http://127.0.0.1:8000/docs
- 📚 Documentation Redoc : http://127.0.0.1:8000/redoc

📄 Alimentation de la base avec des requêtes CURL :
- Le fichier **[`liste_commande_curl.txt`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/liste_commande_curl.txt)** contient une liste complète des commandes curl permettant d'alimenter la base de données.

### 2.2 Exercice 2 : serveur web
Dans cette partie, j'ai intégré un graphique à secteurs en 3D utilisant Google Charts et créé une interface utilisateur dynamique.

📌 Technologies Utilisées :
- FastAPI : Serveur Backend pour transmettre les données.
- Google Charts : Génération du graphique en 3D.
- HTML / CSS : Interface utilisateur et design.

J'ai utilisé le code HTML permettant de créer un graphique à secteurs en 3D via ce **[`lien`](https://developers-dot-devsite-v2-prod.appspot.com/chart/interactive/docs/gallery/piechart)** 
J'ai entré plusieurs prompts sur ChatGPT pour réaliser l'interface web et modifier le serveur pour l'envoi des données :

- 1️⃣1er prompt : ```Peux-tu m'écrire une fonction Python permettant de récupérer les montants de factures et de calculer la somme pour chaque type de facture afin d'établir en pourcentage le montage pour chaque type divisé par le montant total ensuite il faudra modifier le code HTML pour prendre en compte les valeurs envoyés par notre serveur ? ```

- 2️⃣2ème prompt : ```Maintenant, peux-tu afficher sur la page web une liste déroulante permettant à l'utilisateur de choisir un logement parmi celle présente dans notre base de données ? ```

- 3️⃣3ème prompt : ```Merci beaucoup ! Je veux que tu ajoutes une barre de navigation en haut avec le logo à gauche et le texte au centre, et aussi le camembert centré```

- 4️⃣4ème prompt : ```Enfin, je te laisse la liberté de rendre le design plus agréable avec du CSS avec une image en background, en ajoutant des animations comme le survol du logo lorsqu'on clique dessus et d'ailleurs je souhaite que lorsqu'on clique sur le logo ça nous redirige vers la page d'accueil s'il te plaît ?```


 

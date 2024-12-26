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
- Le fichier **[`liste_commande_curl.txt`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/liste_commande_curl.txt)** liste toutes les commandes curl permettant d'alimenter notre base de données.

💻 Nous pouvons lancer l'application en tapant la commande suivante sur le terminal : ```fastapi dev serveur.py```
- Cela démarrera le serveur à l'adresse suivante : http://127.0.0.1:8000/
- 📚 Api docs : http://127.0.0.1:8000/docs
- 📚 Redoc Documentation : http://127.0.0.1:8000/redoc


# 📦 Projet IoT - Logement Éco-Responsable

## 📝 Description du Projet
Ce projet IoT vise à développer une application permettant de gérer un logement éco-responsable. Il inclut :

- 🔌 Surveillance de la consommation énergétique
- 📡 Gestion des capteurs et actionneurs
- 💰 Affichage des économies réalisées
- ⚙️ Configuration pour gérer les logements, pièces et équipements (capteurs/actionneurs)

## 🛠️ Technologies Utilisées
- Backend : FastAPI
- Frontend : HTML/CSS/JavaScript
- Base de données : SQLite

## 🚀 Installation et Lancement

📥Prérequis

Il faut avoir la version Python 3.10+ installé sur son système

📦 Installation des dépendances

Exécutez la commande suivante pour installer les bibliothèques nécessaires :
```bash 
pip install fastapi uvicorn sqlmodel jinja2 python-multipart requests pandas
```
📂 Clonage du projet

Clonez le dépôt GitHub sur votre environnement local :
```bash 
git clone https://github.com/AyoubLADJICI/Logement-eco-responsable.git
cd Logement-eco-responsable
```

🚀 Démarrer l'application 

Lance le serveur FastAPI avec la commande : 
```bash 
fastapi dev main.py
```
ou

```bash 
uvicorn main:app --reload
```

Accédez ensuite à l'application via : **[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)**

📚 Documentation Technique

📝 Partie1.md
- Présentation de l'architecture générale.
- Mise en place de la base de données.
  
📝 Partie2.md
- Configuration et intégration des capteurs/actionneurs.
- Gestion des interactions avec la base de données.
  
📝 Partie3.md
- Développement du Frontend (HTML/CSS/JavaScript).
- Gestion des onglets : Accueil, Consommation, État des Capteurs, Économies, Configuration.
- Explication détaillée des fonctionnalités.
 
📝 liste_commande_curl.txt
- Liste des commandes CURL pour tester les différentes routes API.

📊 Base de Données
- SQLite est utilisé comme système de gestion de base de données.

📊 Schéma UML
- Le fichier [`uml_database.png`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/uml_database.png) présente un diagramme relationnel de la base de données.







# TP IoT - Logement Éco-Responsable

## 🗃️ Partie 1 : Modèle Relationnel de la Base de Données
### 1.1 Spécifications de la base de données
**Question 1 :** Le modèle relationnel de la base de données se trouve dans le fichier :  
**📁 [`uml_database.png`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/uml_database.png)**
- Il a été construit en respectant les **spécifications données dans le sujet**.
- Les **rectangles verts** contiennent les **entités** (les tables) et leurs **attributs associés**.
- Les **losanges rouges** montrent les **relations entre les entités**. 
- Par exemple, un **Logement** peut **contenir une ou plusieurs Pièces** *(1:N)*.
- Un **Logement** peut aussi **générer aucune ou plusieurs Factures** *(0:N)*.

**Question 2 :** Les ordres SQL permettant de détruire toutes les tables existantes dans notre base se trouve dans le fichier :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 15 à 20```
- Cela est possible grâce à la commande ```DROP TABLE IF EXISTS nom_table;```
- Je me suis appuyé sur les ressources disponibles dans le cours de base de données sur Moodle.
- Ce **[`site`](https://www.devart.com/dbforge/sql/studio/sql-server-drop-table.html)** m'a aussi aidé pour répondre à cette question, il présente les différentes façons d'utiliser DROP TABLE dans SQL.

**Question 3 :** Les ordres SQL permettant de créer toutes les tables de notre base se trouve dans le fichier :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 28 à 93```
- Cela est possible grâce à la commande ```CRATE TABLE nom_table(id_nom_table INTEGER PRIMARY KEY AUTOINCREMENT, nom_champ type_champ,..., FOREIGN KEY (id_Ad) REFERENCES Adresse(id_autre_table)); ```
- Je me suis appuyé sur les ressources disponibles dans le cours de base de données sur Moodle.
- J'ai entré le prompt suivant ```Peux-tu me lister tous les types en SQL et dans quels cas est-il judicieux de les utiliser ?``` sur ChatGPT afin de pouvoir associer chaque champ au type adéquat. 
- INTEGER → Pour les identifiants uniques et les références entre tables
- TEXT → Pour les champs pouvant contenir de longues chaînes de caractères
- CHAR(10) → Pour stocker des numéros français strictement composés de 10 chiffres (sans préfixe +33)
- VARCHAR(45) → Pour supporter des adresses IP au format IPv4 et IPv6
- DECIMAL(5,2) → Pour les montants de factures en supposant qu'elles ne dépassent pas 999,99€
- REAL → Pour les champs nécessitant une valeur numérique précise  
- TIMESTAMP → Pour enregistrer automatiquement les dates et heures d'insertion dans la base de données

**Question 4 :** Les ordres SQL permettant de créer un logement avec 4 pièces :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 95 à 103```
- J'ai crée un logement avec 4 pièces distinces : Chambre, Salon, Cuisine, Salle de bain

**Question 5 :** Les ordres SQL permettant de créer au moins 4 types de capteurs/actionneurs :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 105 à 111```
- J'ai crée 5 types de capteurs (Température, Humidité, Consommation électrique, Niveau d'eau, Consommation de gaz) et 2 types d'actionneurs (Volets roulants, Lumières)

**Question 6 :** Les ordres SQL permettant de créer au moins 2 capteurs/actionneurs :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 113 à 123```
- J'ai crée un capteur/actionneur pour chaque type et en l'associant à une pièce spécifique d'un logement

**Question 7 :** Les ordres SQL permettant de créer au moins 2 mesures par capteur/actionneur :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 125 à 143```
- J'ai ajouté 2 mesures par capteur/actionneur dans notre base de donnée

**Question 8 :** Les ordres SQL permettant de créer au moins 4 factures :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 145 à 150```
- J'ai crée 4 factures de types différents (Électricité, Eau, Gaz, Internet)

### 1.2 Remplissage de la base de données
La fonction de remplissage se trouve dans le fichier : **📁 [`remplissage.py`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/remplissage.py)**

- J'ai entré le prompt suivant ```Peux-tu m'aider à écrire une fonction Python pour insérer automatiquement des factures sur un nombre de jours et un logement que je pourrais choisir, en te connectant à ma base de données logement.db ? et en te basant sur la consommation des français pour chaque type de conso afin d'avoir des données réalistes``` sur ChatGPT.

La fonction ajouter_factures permet d'ajouter des factures "réalistes" pour un logement donné sur une période définie (exemple 30 jours). Exemple : ```ajouter_factures(1, 30)```

Les valeurs de consommation et les montants sont calculés en fonction des plages prédéfinies pour chaque type de consommation. La fonction fait également en sorte d'éviter les doublons en vérifiant les factures déjà présentes dans la base de données pour la même date et le même type.


 


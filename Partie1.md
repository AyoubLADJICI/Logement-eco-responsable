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
- Cela est possible grâce à la commande ```DROP TABLE IF EXISTS nom_table```
- Je me suis aidé des ressources présentes dans le cours de base de données sur Moodle.
- Ce **[`site`](https://www.devart.com/dbforge/sql/studio/sql-server-drop-table.html)** m'a aussi aidé pour répondre à cette question, il présente les différentes façons d'utiliser DROP TABLE dans SQL.

**Question 3 :** Les ordres SQL permettant de créer toutes les tables de notre base se trouve dans le fichier :
**📁 [`logement.sql`](https://github.com/AyoubLADJICI/Logement-eco-responsable/blob/main/logement.sql)** ```lignes 28 à 93```
- Cela est possible grâce à la commande ```CRATE TABLE nom_table(id_nom_table INTEGER PRIMARY KEY AUTOINCREMENT, nom_champ type_champ,..., FOREIGN KEY (id_Ad) REFERENCES Adresse(id_autre_table)); ```
- Je me suis aidé des ressources présentes dans le cours de base de données sur Moodle.


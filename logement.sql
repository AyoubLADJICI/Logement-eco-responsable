-- Suppression de la table Logement si elle existe deja
DROP TABLE IF EXISTS Logement;

-- Suppression de la table Piece si elle existe deja
DROP TABLE IF EXISTS Piece;

-- Suppression de la table Capteur/Actionneur si elle existe deja
DROP TABLE IF EXISTS Capteur_Actionneur;

-- Suppression de la table Type de Capteur/Actionneur si elle existe deja
DROP TABLE IF EXISTS Type_capteur_actionneur;

-- Suppression de la table Mesure si elle existe deja
DROP TABLE IF EXISTS Mesure;

-- Suppression de la table Facture si elle existe deja
DROP TABLE IF EXISTS Facture;

-- Creation de la table Logement
CREATE TABLE Logement (
    id_logement INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse_postale TEXT NOT NULL,
    numero_telephone TEXT NOT NULL,
    adresse_ip TEXT NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creation de la table Piece
CREATE TABLE Piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    z INTEGER NOT NULL,
    id_logement INTEGER NOT NULL,
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

-- Creation de la table Capteur/Actionneur
CREATE TABLE Capteur_Actionneur (
    id_capteur_actionneur INTEGER PRIMARY KEY AUTOINCREMENT,
    id_type INTEGER NOT NULL,
    nom TEXT NOT NULL,
    reference_commerciale TEXT NOT NULL,
    reference_piece INTEGER NOT NULL,
    port_communication TEXT NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reference_piece) REFERENCES Piece(id_piece),
    FOREIGN KEY (id_type) REFERENCES Type_Capteur_Actionneur(id_type_capteur_actionneur)
);

-- Creation de la table Type de Capteur/Actionneur
CREATE TABLE Type_Capteur_Actionneur (
    id_type_capteur_actionneur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_type TEXT NOT NULL,
    unite TEXT NOT NULL,
    min_valeur REAL NOT NULL,
    max_valeur REAL NOT NULL
);

-- Creation de la table Mesure
CREATE TABLE Mesure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_capteur_actionneur INTEGER NOT NULL,
    valeur REAL NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_capteur_actionneur) REFERENCES Capteur_Actionneur(id_capteur_actionneur)
);

-- Creation de la table Facture
CREATE TABLE Facture (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_logement INTEGER NOT NULL,
    type_facture TEXT NOT NULL,
    date_facture TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    montant REAL NOT NULL,
    valeur_consommation REAL NOT NULL,
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

INSERT INTO Logement (adresse_postale, numero_telephone, adresse_ip)
VALUES ('1 Allee des Roseaux', '07 78 81 32 32', '192.168.72.93');

INSERT INTO Piece (nom, x, y, z, id_logement) 
VALUES ('Chambre', 5, 2, 0, 1), ('Salon', 3, 1, 0, 1),
('Cuisine', 1, 2, 0, 1), ('Salle de bain', 3, 3, 0, 1); 

INSERT INTO Type_Capteur_Actionneur (nom_type, unite, min_valeur, max_valeur) 
VALUES ('Temperature', '°C', -20, 100), ('Humidite', '%', 0, 100),
('Consommation électrique', 'kWh', 0, 10000), ('Accelerometre', 'm/s²', -156.96, 156.95); 

INSERT INTO Capteur_Actionneur (id_type, nom, reference_commerciale, reference_piece, port_communication) 
VALUES (1, 'DHT11', 'DHT11', 3, '80'), (4, 'ADXL345', 'ADXL345B-REEL', 2, '443'); 

INSERT INTO Mesure (id_capteur_actionneur, valeur) 
VALUES (1, 25.5), (1, 29.7), (2, 93.35), (2, 150.53); 

INSERT INTO Facture (id_logement, type_facture, montant, valeur_consommation) 
VALUES (1, 'Electricite', 75.50, 250), (1, 'Eau', 30.00, 15),
(1, 'Gaz', 40.00, 20), (1, 'Internet', 15.00, 5); 
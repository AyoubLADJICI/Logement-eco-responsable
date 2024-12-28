-- ====================================================================
-- 🏠 TP IoT - Logement Éco-Responsable : logement.sql
-- Auteur : Ayoub LADJICI
-- Description : Ce fichier contient les instructions SQL pour :
-- 1. Supprimer des tables existantes.
-- 2. Créer des tables.
-- 3. Ajouter des données pour initialiser notre base de données.
-- Source : Moodle IoT Cours Base de Données (pages 55,57,58,61)
-- https://www.devart.com/dbforge/sql/studio/sql-server-drop-table.html
-- ====================================================================

-- ===================================================================================================
-- Question 2 : Ajouter les ordres SQL pour supprimer les tables existantes dans notre base de données
-- ===================================================================================================
DROP TABLE IF EXISTS Logement;
DROP TABLE IF EXISTS Facture;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Capteur_Actionneur;
DROP TABLE IF EXISTS Type_capteur_actionneur;
DROP TABLE IF EXISTS Mesure;

-- ==================================================================================
-- Question 3 : Ajouter les ordres SQL pour créer les tables de notre base de données
-- ==================================================================================

-- 📦 Table Logement
-- Cette table représente un logement unique.
CREATE TABLE Logement (
    id_logement INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse_postale TEXT NOT NULL,
    numero_telephone CHAR(10) NOT NULL,
    adresse_ip VARCHAR(45) NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP --Date et heure d'insertion dans la base
);

-- 📦 Table Facture
-- Enregistre les factures associées à un logement.
CREATE TABLE Facture (
    id_facture INTEGER PRIMARY KEY AUTOINCREMENT,
    id_logement INTEGER NOT NULL,
    type_facture TEXT NOT NULL,
    date_facture TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    montant DECIMAL(5,2) NOT NULL,
    valeur_consommation REAL NOT NULL,
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

-- 📦 Table Piece
-- Chaque logement peut contenir plusieurs pièces.
CREATE TABLE Piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    --Coordonnées 3D pour localiser la pièce dans le logement
    coord_x INTEGER NOT NULL,
    coord_y INTEGER NOT NULL,
    coord_z INTEGER NOT NULL,
    id_logement INTEGER NOT NULL, --Référence au logement auquel appartient la pièce
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

-- 📦 Table TypeCapteurActionneur
-- Définit les types de capteurs/actionneurs disponibles.
CREATE TABLE Capteur_Actionneur (
    id_capteur_actionneur INTEGER PRIMARY KEY AUTOINCREMENT,
    id_type INTEGER NOT NULL,
    nom TEXT NOT NULL,
    reference_commerciale TEXT NOT NULL,
    reference_piece INTEGER NOT NULL, --Référence à la pièce où le capteur est installé.
    port_communication TEXT NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reference_piece) REFERENCES Piece(id_piece),
    FOREIGN KEY (id_type) REFERENCES Type_Capteur_Actionneur(id_type_capteur_actionneur)
);

-- 📦 Table CapteurActionneur
-- Chaque pièce peut contenir plusieurs capteurs/actionneurs de différents types.
CREATE TABLE Type_Capteur_Actionneur (
    id_type_capteur_actionneur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_type TEXT NOT NULL,
    unite TEXT NOT NULL,
    min_valeur REAL NOT NULL,
    max_valeur REAL NOT NULL
);

-- 📦 Table Mesure
-- Les capteurs/actionneurs enregistrent des mesures.
CREATE TABLE Mesure (
    id_mesure INTEGER PRIMARY KEY AUTOINCREMENT,
    id_capteur_actionneur INTEGER NOT NULL, --Référence au capteur qui a enregistré la mesure
    valeur REAL NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_capteur_actionneur) REFERENCES Capteur_Actionneur(id_capteur_actionneur)
);

-- ======================================================
-- 🏠 Question 4 : Création d'un Logement et de 4 Pièces
-- ======================================================
INSERT INTO Logement (adresse_postale, numero_telephone, adresse_ip)
VALUES ('1 Allee des Roseaux 93600 Aulnay-Sous-Bois', '0778813232', '192.168.72.93');

INSERT INTO Piece (nom, coord_x, coord_y, coord_z, id_logement) 
VALUES ('Chambre', 5, 2, 0, 1), ('Salon', 3, 1, 0, 1),
('Cuisine', 1, 2, 0, 1), ('Salle de bain', 3, 3, 0, 1); 

-- ============================================================
-- 📡 Question 5 : Création de 7 Types de Capteurs/Actionneurs
-- ============================================================
INSERT INTO Type_Capteur_Actionneur (nom_type, unite, min_valeur, max_valeur) 
VALUES ('Temperature', '°C', -20, 50), ('Humidite', '%', 0, 100), ('Consommation electrique', 'kWh', 0, 1000),
('Niveau eau', 'm3', 0, 100), ('Consommation gaz', 'm3', 0, 100), ('Volets Roulants', '%', 0, 100),
('Lumieres', 'ON/OFF', 0, 1);

-- ===================================================
-- 🔌 Question 6 : Création de 7 Capteurs/Actionneurs
-- ===================================================
INSERT INTO Capteur_Actionneur (id_type, nom, reference_commerciale, reference_piece, port_communication) 
VALUES (1, 'Capteur de température DHT11', 'TEMP-001', 1, 'UART1'), --pour la chambre
(2, 'Capteur d humidité DHT11', 'HUM-001', 1, 'UART2'), --pour la chambre
(3, 'Capteur de Consommation Electrique ACS712', 'ELEC-001', 2, 'UART3'), --pour le salon
(4, 'Capteur de Niveau d eau C7249', 'EAU-001', 4, 'SPI1'), --pour la salle de Bain 
(5, 'Capteur de Consommation de Gaz MQ-2', 'GAZ-001', 3, 'SPI2'), --pour la cuisine
(6, 'Actionneur de Volets Roulants', 'VOLET-001', 2, 'I2C1'), --pour le salon
(7, 'Actionneur de Lumieres', 'LUM-001', 2, 'I2C2'); --pour le salon

-- ============================================================
-- 📊 Question 7 : Création de 2 Mesures par Capteur/Actionneur
-- ============================================================
INSERT INTO Mesure (id_capteur_actionneur, valeur) 
VALUES 
(1, 22.5), -- Température mesurée : 22.5°C
(1, 23.1), -- Température mesurée : 23.1°C
(2, 45.0), -- Humidité mesurée : 45%
(2, 50.3), -- Humidité mesurée : 50.3%
(3, 4.7), -- Consommation électrique : 4.7 kWh
(3, 3.2), -- Consommation électrique : 3.2 kWh
(4, 15.4), -- Niveau d'eau : 15.4 m³
(4, 16.1), -- Niveau d'eau : 16.1 m³
(5, 32.5), -- Consommation de gaz : 32.5 m³
(5, 30.8), -- Consommation de gaz : 30.8 m³
(6, 50.0), -- Position des volets : 50% ouverts
(6, 75.0), -- Position des volets : 75% ouverts
(7, 1), -- Lumière allumée (ON)
(7, 0); -- Lumière éteinte (OFF)

-- =======================================
-- 💳 Question 8 : Création de 4 Factures
-- =======================================
INSERT INTO Facture (id_logement, type_facture, montant, valeur_consommation) 
VALUES (1, 'Electricite', 75.50, 250.00), (1, 'Eau', 30.00, 15.21),
(1, 'Gaz', 40.00, 20.14), (1, 'Internet', 15.00, 50.75);
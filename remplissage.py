import sqlite3
import random
from datetime import datetime, timedelta

# Ouverture/initialisation de la base de données
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Fonction pour insérer des factures dans la base de données
def ajouter_factures(id_logement, nb_jours):
    types_facture = ['Electricite', 'Eau', 'Gaz', 'Internet']
    today = datetime.now()

    plages_consommation = {
        'Electricite': (1, 8),  # 1 à 8 kWh
        'Eau': (0.5, 3),        # 0.5 à 3 m³
        'Gaz': (2, 10),         # 2 à 10 m³
        'Internet': (50, 300)   # 50 à 300 Go
    }

    for jour in range(nb_jours):
        date_facture = (today - timedelta(days=jour)).strftime('%Y-%m-%d')
        for type_facture in types_facture:
            # Vérifier s'il existe déjà une facture pour ce type et cette date
            c.execute("""
                SELECT COUNT(*) FROM Facture
                WHERE id_logement = ? AND type_facture = ? AND DATE(date_facture) = DATE(?)
            """, (id_logement, type_facture, date_facture))
            
            if c.fetchone()[0] == 0:  # Si aucune facture similaire n'existe
                # Générer une valeur de consommation dans la plage définie
                min_val, max_val = plages_consommation.get(type_facture, (0, 0))
                consommation = round(random.uniform(min_val, max_val), 2)
                
                # Montant est calculé directement ici pour éviter une valeur incohérente
                tarifs = {
                    'Electricite': 0.15,  # €/kWh
                    'Eau': 2.0,          # €/m³
                    'Gaz': 0.09,         # €/kWh ou m³
                    'Internet': 0.00495  # €/Go
                }
                montant = round(consommation * tarifs.get(type_facture, 0), 2)

                c.execute("""
                    INSERT INTO Facture (id_logement, type_facture, date_facture, montant, valeur_consommation)
                    VALUES (?, ?, ?, ?, ?)
                """, (id_logement, type_facture, date_facture, montant, consommation))
    print(f"Factures ajoutées pour {nb_jours} jours pour le logement {id_logement}.")

def trier_factures():
    # Trier les factures par date et par ID
    c.execute("""
        SELECT *
        FROM Facture
        ORDER BY date_facture ASC;
    """)
    factures_triees = c.fetchall()

    # Supprimer les anciennes factures
    c.execute("DELETE FROM Facture;")

    # Réinsérer les factures triées
    for facture in factures_triees:
        c.execute("""
            INSERT INTO Facture (id, id_logement, type_facture, date_facture, montant, valeur_consommation)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (
            facture['id'],
            facture['id_logement'],
            facture['type_facture'],
            facture['date_facture'],
            facture['montant'],
            facture['valeur_consommation']
        ))
        print(facture['date_facture'])
    print("Factures triées et réinsérées.")

def ajouter_pieces_pour_logement(id_logement, pieces):
    """
    Attribue des pièces à un logement spécifique dans la base de données.

    :param id_logement: ID du logement auquel attribuer les pièces
    :param pieces: Liste de dictionnaires contenant les informations des pièces (nom, x, y, z)
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    for piece in pieces:
        c.execute("""
            INSERT INTO Piece (nom, x, y, z, id_logement)
            VALUES (?, ?, ?, ?, ?)
        """, (piece['nom'], piece['x'], piece['y'], piece['z'], id_logement))
    
    conn.commit()
    conn.close()
    print(f"Pièces ajoutées pour le logement {id_logement}.")

# Exemple d'utilisation
pieces_logement_2 = [
    {'nom': 'Salon', 'x': 1, 'y': 2, 'z': 0},
    {'nom': 'Cuisine', 'x': 3, 'y': 4, 'z': 0},
    {'nom': 'Salle de bain', 'x': 5, 'y': 6, 'z': 0},
    {'nom': 'Chambre', 'x': 7, 'y': 8, 'z': 0}
]

#ajouter_pieces_pour_logement(id_logement=2, pieces=pieces_logement_2)
import random

def ajouter_capteurs_par_piece(session, logement_id, types_capteurs, capteurs_par_type, capteurs_par_piece):
    """
    Ajoute des capteurs à chaque pièce d'un logement.

    Args:
        session: Session de la base de données.
        logement_id (int): ID du logement.
        types_capteurs (list): Liste des types de capteurs disponibles (nom_type).
        capteurs_par_type (int): Nombre de capteurs à créer pour chaque type.
        capteurs_par_piece (int): Nombre minimal de capteurs par pièce.
    """
    # Récupérer les pièces du logement
    pieces = session.exec(select(Piece).where(Piece.id_logement == logement_id)).all()

    if not pieces:
        print(f"Aucune pièce trouvée pour le logement {logement_id}")
        return

    # Récupérer les types de capteurs disponibles
    types_disponibles = session.exec(select(Type_Capteur_Actionneur).where(Type_Capteur_Actionneur.nom_type.in_(types_capteurs))).all()
    if not types_disponibles:
        print("Aucun type de capteur disponible correspondant.")
        return

    # Ajouter des capteurs pour chaque pièce
    for piece in pieces:
        print(f"Ajout de capteurs pour la pièce : {piece.nom}")

        # Assurer un nombre minimal de capteurs par pièce
        for _ in range(capteurs_par_piece):
            type_capteur = random.choice(types_disponibles)
            nouveau_capteur = Capteur_Actionneur(
                id_type=type_capteur.id_type_capteur_actionneur,
                nom=f"{type_capteur.nom_type} - {piece.nom}",
                reference_commerciale=f"REF-{type_capteur.nom_type}-{random.randint(1000, 9999)}",
                reference_piece=piece.id_piece,
                port_communication="OFF"  # Par défaut, désactivé
            )
            session.add(nouveau_capteur)

        # Ajouter des capteurs supplémentaires par type
        for type_capteur in types_disponibles:
            for _ in range(capteurs_par_type):
                nouveau_capteur = Capteur_Actionneur(
                    id_type=type_capteur.id_type_capteur_actionneur,
                    nom=f"{type_capteur.nom_type} - {piece.nom}",
                    reference_commerciale=f"REF-{type_capteur.nom_type}-{random.randint(1000, 9999)}",
                    reference_piece=piece.id_piece,
                    port_communication="OFF"  # Par défaut, désactivé
                )
                session.add(nouveau_capteur)

    session.commit()
    print(f"Capteurs ajoutés pour les pièces du logement {logement_id}.")

from sqlmodel import Session

# Exemple d'utilisation
with Session(engine) as session:
    ajouter_capteurs_par_piece(
        session=session,
        logement_id=2,  # ID du logement cible
        types_capteurs=["Temperature", "Humidite", "Consommation électrique", "Gaz"],  # Types de capteurs
        capteurs_par_type=2,  # Nombre de capteurs par type à ajouter
        capteurs_par_piece=1  # Nombre minimal de capteurs par pièce
    )

# Appel des fonctions
#c.execute("DELETE FROM Facture;")
#c.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'Facture';")
#ajouter_factures(id_logement=2, nb_jours=120)  # Ajout de factures sur les 30 derniers jours
#trier_factures()  # Tri des factures par date
#c.execute("SELECT * FROM Facture ORDER BY date_facture ASC;")
# Validation des modifications
conn.commit()
# Fermeture de la connexion
conn.close()
print("Données ajoutées et triées avec succès dans la base de données.")



# Appel des fonctions pour ajouter des données 
#ajouter_mesures(id_capteur_actionneur = random.randint(1,2), nb_mesures = 1000)  
#ajouter_mesures(id_capteur_actionneur = random.randint(1,2), nb_mesures = 1000)

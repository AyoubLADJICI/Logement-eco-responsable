import sqlite3, random
from datetime import datetime, timedelta

# Ouverture/initialisation de la base de données
conn = sqlite3.connect('logement.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Fonction pour ajouter des factures dans la base de données
def ajouter_factures(id_logement, nb_jours):
    types_facture = ['Electricite', 'Eau', 'Gaz', 'Internet']
    today = datetime.now()

    if (id_logement == 1):
        plages_consommation = {
            'Electricite': (1, 3),  # 1 à 3 kWh
            'Eau': (5, 10),         # 5 à 10 m³
            'Gaz': (10, 20),        # 10 à 20 m³
            'Internet': (50, 100)   # 50 à 100 Go
        }
    elif (id_logement == 2): 
        plages_consommation = {
            'Electricite': (10, 20),  # 10 à 20 kWh
            'Eau': (0.5, 2),          # 0.5 à 2 m³
            'Gaz': (1, 5),            # 1 à 5 m³
            'Internet': (200, 500)    # 200 à 500 Go
        }
    elif (id_logement == 3): 
        plages_consommation = {
            'Electricite': (0.5, 2),  # 3 à 2 kWh
            'Eau': (0.1, 1),          # 0.1 à 1 m³
            'Gaz': (0.1, 0.5),        # 0.1 à 0.5 m³
            'Internet': (10, 50)      # 10 à 50 Go
        }
    else:
        plages_consommation = {
            'Electricite': (1, 6),  # 1 à 6 kWh
            'Eau': (0.5, 3),        # 0.5 à 3 m³
            'Gaz': (2, 10),         # 2 à 10 m³
            'Internet': (50, 150)   # 50 à 150 Go
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
                
                tarifs = {
                    'Electricite': 0.2516,  # €/kWh
                    'Eau': 1.15,            # €/m³
                    'Gaz': 0.923,           # €/m³
                    'Internet': 0.23        # €/Go
                }
                montant = round(consommation * tarifs.get(type_facture, 0), 2)

                c.execute("""
                    INSERT INTO Facture (id_logement, type_facture, date_facture, montant, valeur_consommation)
                    VALUES (?, ?, ?, ?, ?)
                """, (id_logement, type_facture, date_facture, montant, consommation))
    print(f"✅Factures ajoutées sur les {nb_jours} derniers jours pour le logement {id_logement}.")
    
    
# ============================================================
# 📊 Fonction pour ajouter des mesures dans la base de données
# ============================================================

def ajouter_mesures(nb_jours):
    """
    Ajoute des mesures pour chaque capteur/actionneur dans la base de données.
    :param nb_jours: Nombre de jours pour lesquels générer des mesures.
    """
    today = datetime.now()
    
    plages_mesures = {
        'Temperature': (-20, 50),  # °C
        'Humidite': (0, 100),      # %
        'Consommation electrique': (0, 1000),  # kWh
        'Niveau eau': (0, 100),    # m³
        'Consommation gaz': (0, 100),  # m³
        'Volets': (0, 100),        # % ouvert
        'Lumieres': (0, 1)         # ON/OFF (0 ou 1)
    }
    
    # Récupérer tous les capteurs/actionneurs
    c.execute("SELECT id_capteur_actionneur, id_type FROM Capteur_Actionneur")
    capteurs = c.fetchall()
    
    for jour in range(nb_jours):
        date_mesure = (today - timedelta(days=jour)).strftime('%Y-%m-%d %H:%M:%S')
        for capteur in capteurs:
            id_capteur = capteur['id_capteur_actionneur']
            id_type = capteur['id_type']
            
            # Récupérer le type du capteur/actionneur pour définir la plage
            c.execute("SELECT nom_type FROM Type_Capteur_Actionneur WHERE id_type_capteur_actionneur = ?", (id_type,))
            type_capteur = c.fetchone()['nom_type']
            
            # Obtenir la plage de valeurs
            min_val, max_val = plages_mesures.get(type_capteur, (0, 0))
            valeur = round(random.uniform(min_val, max_val), 2)
            
            # Insérer la mesure dans la base de données
            c.execute("""
                INSERT INTO Mesure (id_capteur_actionneur, valeur, date_insertion)
                VALUES (?, ?, ?)
            """, (id_capteur, valeur, date_mesure))
    
    print(f"✅ Mesures ajoutées sur les {nb_jours} derniers jours pour tous les capteurs/actionneurs.")

#Appel des fonctions
ajouter_factures(13, 10)
ajouter_mesures(30)

# Validation des modifications
conn.commit()
# Fermeture de la connexion
conn.close()
print("✅Données ajoutées et triées avec succès dans la base de données.") 

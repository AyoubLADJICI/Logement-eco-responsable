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
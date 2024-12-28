from typing import Annotated,Optional, List
from fastapi import Depends, FastAPI, HTTPException, Query, Request, Path, Body
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import pandas as pd
from datetime import datetime, timedelta 
from sqlalchemy.sql import func

# Modèles de données SQLModel
class Logement(SQLModel, table=True):
    id_logement : int = Field(default = None, primary_key = True)
    adresse_postale : str = Field(index=True)
    numero_telephone : str = Field(index=True)
    adresse_ip : str = Field(index=True)
    date_insertion: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Piece(SQLModel, table=True):
    id_piece : int = Field(default = None, primary_key = True)
    nom : str = Field(index=True)
    coord_x : int = Field(index=True)
    coord_y : int = Field(index=True)
    coord_z : int = Field(index=True)
    id_logement : int = Field(index=True) 

class Capteur_Actionneur(SQLModel, table=True):
    id_capteur_actionneur : int = Field(default = None, primary_key = True)
    id_type : int = Field(index=True)
    nom : str = Field(index=True)
    reference_commerciale : str = Field(index=True)
    reference_piece : int = Field(index=True)
    port_communication : str = Field(index=True)
    date_insertion: Optional[datetime] = Field(default_factory=datetime.utcnow)
    etat: str = Field(default="ON")  # Nouveau champ ON/OFF (Ajoute lors de la partie 3)

class Type_Capteur_Actionneur(SQLModel, table=True):
    id_type_capteur_actionneur : int = Field(default = None, primary_key = True)
    nom_type : str = Field(index=True)
    unite : str = Field(index=True)
    min_valeur : float = Field(index=True)
    max_valeur : float = Field(index=True)
 
class Mesure(SQLModel, table=True):
    id_mesure: int = Field(default=None, primary_key=True)
    id_capteur_actionneur: int
    valeur: float
    date_insertion: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Facture(SQLModel, table=True):
    id_facture: int = Field(default=None, primary_key=True)
    id_logement: int = Field(index=True)
    type_facture: str = Field(index=True)
    date_facture: Optional[datetime] = Field(default_factory=datetime.utcnow)
    montant: float = Field(index=True)
    valeur_consommation: float = Field(index=True)

# Creation de notre moteur SQLModel 
# pour permettre a notre code de se connecter a notre base de donnees
sqlite_file_name = "logement.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

#L'utilisation de check_same_thread=False permet à FastAPI d'utiliser la même base de données SQLite dans différents threads
#Ceci est nécessaire car une seule requête peut utiliser plus d'un thread (par exemple dans les dépendances)
#toutefois FastAPI s'assure qu'une session SQLModel distincte est créée pour chaque requête HTTP
connect_args = {"check_same_thread" : False} 
engine = create_engine(sqlite_url, connect_args=connect_args)    

# Fonction permettant de creer les tables pour
# tous les modeles de table dans notre BDD
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Fonction permettant de stocker les objets en memoire
# Utilise le moteur pour communiquer avec la BDD
def get_session():
    with Session(engine) as session:
        yield session #Garantit une seule session pour chaque requete

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
# Monter le dossier static pour servir les fichiers CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration des templates
templates = Jinja2Templates(directory="templates")

# Creation des tables de la BDD au demarrage de l'application
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#Chaque modele SQLModel est un modele Pydantic
#ce qui facilite la conversion des données entre
#les formats json et Python
@app.post("/logement/")
def create_logement(logement: Logement, session: Session = Depends(get_session)):
    session.add(logement)
    session.commit()
    session.refresh(logement)
    return logement

#Fonction permettant de lire les logements de la base de données
#a l'aide de la fonction select
@app.get("/logements/")
def read_logement(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)]=100,):
    logements = session.exec(select(Logement).offset(offset).limit(limit)).all()
    return logements

@app.get("/logements/{id_logement}")
def read_logement(id_logement: int, session: Session = Depends(get_session)):
    logement = session.get(Logement, id_logement)
    if not logement:
        raise HTTPException(status_code=404, detail="Logement not found")
    return logement

@app.delete("/logements/{logement_id}")
def delete_logement(id_logement: int, session: Session = Depends(get_session)):
    logement = session.get(Logement, id_logement)
    if not logement:
        raise HTTPException(status_code=404, detail="Logement Not Found")
    session.delete(logement)
    session.commit()
    return {"ok": True}

# Endpoints pour Piece
@app.post("/piece/")
def create_piece(piece: Piece, session: Session = Depends(get_session)):
    session.add(piece)
    session.commit()
    session.refresh(piece)
    return piece

@app.get("/pieces/")
def read_pieces(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    pieces = session.exec(select(Piece).offset(offset).limit(limit)).all()
    return pieces

@app.get("/pieces/{id_piece}")
def read_piece(id_piece: int, session: Session = Depends(get_session)):
    piece = session.get(Piece, id_piece)
    if not piece:
        raise HTTPException(status_code=404, detail="Piece not found")
    return piece

@app.delete("/pieces/{id_piece}")
def delete_piece(id_piece: int, session: Session = Depends(get_session)):
    piece = session.get(Piece, id_piece)
    if not piece:
        raise HTTPException(status_code=404, detail="Piece not found")
    session.delete(piece)
    session.commit()
    return {"ok": True}

# Endpoints pour Capteur_Actionneur
@app.post("/capteur_actionneur/")
def create_capteurs_actionneurs(capteurs: List[Capteur_Actionneur], session: Session = Depends(get_session)):
    try:
        for capteur in capteurs:
            session.add(capteur)
        session.commit()
        for capteur in capteurs:
            session.refresh(capteur)
        return {"message": "Capteurs ajoutés avec succès"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Erreur lors de l'ajout des capteurs : {str(e)}")

@app.get("/capteurs_actionneurs/")
def read_capteurs_actionneurs(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    capteurs_actionneurs = session.exec(select(Capteur_Actionneur).offset(offset).limit(limit)).all()
    return capteurs_actionneurs

@app.get("/capteurs_actionneurs/{id_capteur_actionneur}")
def read_capteur_actionneur(id_capteur_actionneur: int, session: Session = Depends(get_session)):
    capteur_actionneur = session.get(Capteur_Actionneur, id_capteur_actionneur)
    if not capteur_actionneur:
        raise HTTPException(status_code=404, detail="Capteur/Actionneur not found")
    return capteur_actionneur

@app.delete("/capteurs_actionneurs/{id_capteur_actionneur}")
def delete_capteur_actionneur(id_capteur_actionneur: int, session: Session = Depends(get_session)):
    capteur_actionneur = session.get(Capteur_Actionneur, id_capteur_actionneur)
    if not capteur_actionneur:
        raise HTTPException(status_code=404, detail="Capteur/Actionneur not found")
    session.delete(capteur_actionneur)
    session.commit()
    return {"ok": True}

# Endpoints pour Type_Capteur_Actionneur
@app.post("/type_capteur_actionneur/")
def create_type_capteur_actionneur(type_capteur_actionneur: Type_Capteur_Actionneur, session: Session = Depends(get_session)):
    session.add(type_capteur_actionneur)
    session.commit()
    session.refresh(type_capteur_actionneur)
    return type_capteur_actionneur

@app.get("/types_capteurs_actionneurs/")
def read_types_capteurs_actionneurs(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    types_capteurs_actionneurs = session.exec(select(Type_Capteur_Actionneur).offset(offset).limit(limit)).all()
    return types_capteurs_actionneurs

@app.get("/types_capteurs_actionneurs/{id_type_capteur_actionneur}")
def read_type_capteur_actionneur(id_type_capteur_actionneur: int, session: Session = Depends(get_session)):
    type_capteur_actionneur = session.get(Type_Capteur_Actionneur, id_type_capteur_actionneur)
    if not type_capteur_actionneur:
        raise HTTPException(status_code=404, detail="Type Capteur/Actionneur not found")
    return type_capteur_actionneur

@app.delete("/types_capteurs_actionneurs/{id_type_capteur_actionneur}")
def delete_type_capteur_actionneur(id_type_capteur_actionneur: int, session: Session = Depends(get_session)):
    type_capteur_actionneur = session.get(Type_Capteur_Actionneur, id_type_capteur_actionneur)
    if not type_capteur_actionneur:
        raise HTTPException(status_code=404, detail="Type Capteur/Actionneur not found")
    session.delete(type_capteur_actionneur)
    session.commit()
    return {"ok": True}

# Endpoints pour Mesure
@app.post("/mesures/")
def create_mesure(mesure: Mesure, session: Session = Depends(get_session)):
    session.add(mesure)
    session.commit()
    session.refresh(mesure)
    return mesure

@app.get("/mesures/")
def read_mesures(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    mesures = session.exec(select(Mesure).offset(offset).limit(limit)).all()
    return mesures

@app.delete("/mesures/{id}")
def delete_mesure(id: int, session: Session = Depends(get_session)):
    mesure = session.get(Mesure, id)
    if not mesure:
        raise HTTPException(status_code=404, detail="Mesure not found")
    session.delete(mesure)
    session.commit()
    return {"ok": True}

# Endpoints pour Facture
@app.post("/factures/")
def create_facture(facture: Facture, session: Session = Depends(get_session)):
    session.add(facture)
    session.commit()
    session.refresh(facture)
    return facture

@app.get("/factures/")
def read_factures(session: Session = Depends(get_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    factures = session.exec(select(Facture).offset(offset).limit(limit)).all()
    return factures

@app.delete("/factures/{id}")
def delete_facture(id: int, session: Session = Depends(get_session)):
    facture = session.get(Facture, id)
    if not facture:
        raise HTTPException(status_code=404, detail="Facture not found")
    session.delete(facture)
    session.commit()
    return {"ok": True}

@app.get("/factures/chart", response_class=HTMLResponse)
async def chart_factures(request: Request, session: Session = Depends(get_session), id_logement: int = None):
    """
    Affiche les factures sous forme de camembert 3D.
    Si id_logement est fourni, filtre les factures par logement.
    """
    query = select(Facture)
    if id_logement:
        query = query.where(Facture.id_logement == id_logement)

    factures = session.exec(query).all()

    # Regrouper par type et sommer les montants
    totals = {}
    for facture in factures:
        totals[facture.type_facture] = totals.get(facture.type_facture, 0) + facture.montant

    # Préparer les données pour Google Charts
    data = [["Type de Facture", "Montant Total"]]
    for type_facture, total in totals.items():
        data.append([type_facture, total])

    # Récupérer la liste des logements pour la liste déroulante
    logements = session.exec(select(Logement.id_logement, Logement.adresse_postale)).all()
    logements_list = [{"id": logement[0], "adresse": logement[1]} for logement in logements]

    return templates.TemplateResponse(
        "chart.html",
        {"request": request, "data": data, "logements": logements_list, "selected_id": id_logement}
    )
    
def fetch_open_meteo_weather(latitude, longitude):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "relative_humidity_2m", "rain"]
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Déclenche une exception pour les erreurs HTTP
        data = response.json()

        if "hourly" not in data:
            raise ValueError("Données horaires manquantes dans la réponse.")

        # Process data
        hourly_data = {
            "date": data["hourly"]["time"],
            "temperature_2m": data["hourly"]["temperature_2m"],
            "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
            "rain": data["hourly"]["rain"]
        }
        return pd.DataFrame(hourly_data)
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Erreur de connexion à Open-Meteo : {str(e)}")
    except KeyError as e:
        raise ValueError(f"Clé manquante dans la réponse : {str(e)}")

@app.get("/openmeteo/{latitude}/{longitude}")
def get_open_meteo_weather(latitude: float, longitude: float):
    try:
        data = fetch_open_meteo_weather(latitude, longitude)
        return JSONResponse(content=data.to_dict(orient="records"))
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur interne : {str(e)}")

@app.get("/openmeteo/", response_class=HTMLResponse)
async def display_open_meteo_data(request: Request):
    """
    Affiche la page HTML pour saisir les coordonnées et afficher les données météo en tableau.
    """
    return templates.TemplateResponse("meteo.html", {"request": request})

# Routes pour servir les pages HTML
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("accueil.html", {"request": request})

@app.get("/confidentialite.html", response_class=HTMLResponse)
async def confidentialite_page(request: Request):
    return templates.TemplateResponse("confidentialite.html", {"request": request})

@app.get("/consommation", response_class=HTMLResponse)
async def consommation(request: Request):
    return templates.TemplateResponse("consommation.html", {"request": request})

@app.get("/etat_capteurs", response_class=HTMLResponse)
async def etat_capteurs(request: Request):
    return templates.TemplateResponse("etat_capteurs.html", {"request": request})

@app.get("/economies", response_class=HTMLResponse)
async def economies(request: Request):
    return templates.TemplateResponse("economies.html", {"request": request})

@app.get("/configuration", response_class=HTMLResponse)
async def configuration(request: Request):
    return templates.TemplateResponse("configuration.html", {"request": request})

@app.get("/api/statistics")
def get_statistics(session: Session = Depends(get_session)):
    # Récupérer les statistiques
    num_logements = len(session.exec(select(Logement)).all())
    num_types_capteurs = len(session.exec(select(Type_Capteur_Actionneur)).all())
    num_capteurs = len(session.exec(select(Capteur_Actionneur)).all())
    num_mesures = len(session.exec(select(Mesure)).all())

    return {
        "num_logements": num_logements,
        "num_types_capteurs": num_types_capteurs,
        "num_capteurs": num_capteurs,
        "num_mesures": num_mesures,
    }

@app.get("/api/logements")
def get_logements(session: Session = Depends(get_session)):
    logements = session.exec(select(Logement)).all()
    return [{"id_logement": logement.id_logement, "adresse": logement.adresse_postale, "IP": logement.adresse_ip, "Tel": logement.numero_telephone} for logement in logements]

@app.get("/api/consommation")
def get_consumption_data(session: Session = Depends(get_session), logement_id: Optional[int] = None):
    # Calculer la date de 7 jours en arrière
    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)

    # Construire la requête avec ou sans filtre logement
    query = select(Facture).where(Facture.date_facture >= seven_days_ago).order_by(Facture.date_facture.asc())

    if logement_id:
        query = query.where(Facture.id_logement == logement_id)

    # Récupérer les factures
    factures = session.exec(query).all()
    data = []
    for facture in factures:
        data.append({
            "type": facture.type_facture,      # Type de consommation
            "montant": facture.montant,        # Montant de la facture
            "consommation": facture.valeur_consommation,  # Valeur consommée
            "date": facture.date_facture       # Date de la facture
        })
    return data

@app.get("/api/pieces_capteurs")
def get_pieces_capteurs(logement_id: int, session: Session = Depends(get_session)):
    pieces = session.exec(
        select(Piece).where(Piece.id_logement == logement_id)
    ).all()

    result = []
    for piece in pieces:
        capteurs = session.exec(
            select(Capteur_Actionneur)
            .where(Capteur_Actionneur.reference_piece == piece.id_piece)
        ).all()
        result.append({
            "nom": piece.nom,
            "capteurs": [
                {
                    "id_capteur_actionneur": capteur.id_capteur_actionneur,
                    "nom": capteur.nom,
                    "reference_commerciale": capteur.reference_commerciale,
                    "port_communication" : capteur.port_communication,
                    "etat": capteur.etat
                }
                for capteur in capteurs
            ]
        })
    return result

@app.post("/api/capteur_toggle/{capteur_id}")
def toggle_capteur(capteur_id: int, session: Session = Depends(get_session)):
    capteur = session.get(Capteur_Actionneur, capteur_id)
    if not capteur:
        raise HTTPException(status_code=404, detail="Capteur non trouvé")

    # Validation de l'état actuel avant le basculement
    if capteur.etat not in ["ON", "OFF"]:
        raise HTTPException(status_code=400, detail="État invalide pour le basculement")
    
    # Basculer l'état ON/OFF
    capteur.etat = "OFF" if capteur.etat == "ON" else "ON"

    session.add(capteur)
    session.commit()
    session.refresh(capteur)

    return {"success": True, "etat": capteur.etat}

@app.get("/api/economies")
def get_economies(logement_id: int, session: Session = Depends(get_session)):
    data = {
        "electricite": [],
        "eau": [],
        "gaz": [],
        "internet": []
    }

    query = select(
        func.strftime("%Y-%m", Facture.date_facture).label("mois"),
        Facture.type_facture,
        func.sum(Facture.montant).label("montant")
    ).where(Facture.id_logement == logement_id).group_by("mois", Facture.type_facture)

    results = session.exec(query).all()
    previous_totals = {}

    for mois, type_facture, montant in results:
        economie = 0
        if type_facture in previous_totals:
            economie = ((previous_totals[type_facture] - montant) / previous_totals[type_facture]) * 100
        previous_totals[type_facture] = montant

        data[type_facture.lower()].append({
            "mois": mois,
            "montant": montant,
            "economie": round(economie, 2)
        })

    return data



# ➕ Ajouter un logement
@app.post("/api/logements")
def add_logement(logement: Logement, session: Session = Depends(get_session)):
    session.add(logement)
    session.commit()
    session.refresh(logement)
    return {"success": True, "id": logement.id_logement}


# ✏️ Modifier un logement
# ✅ Route PUT pour modifier un logement
@app.put("/api/logements/{id_logement}")
def modifier_logement(
    id_logement: int = Path(..., description="ID du logement à modifier"),
    adresse_postale: str = Body(..., description="Nouvelle adresse postale"),
    numero_telephone: str = Body(..., description="Nouveau numéro de téléphone"),
    adresse_ip: str = Body(..., description="Nouvelle adresse IP"),
    session: Session = Depends(get_session)
):
    """
    Modifier les informations d'un logement existant.
    """
    # ✅ Récupération du logement existant
    db_logement = session.get(Logement, id_logement)
    if not db_logement:
        raise HTTPException(status_code=404, detail="Logement non trouvé")

    # ✅ Mise à jour des champs
    db_logement.adresse_postale = adresse_postale
    db_logement.numero_telephone = numero_telephone
    db_logement.adresse_ip = adresse_ip
    db_logement.date_insertion = datetime.utcnow()

    session.commit()
    session.refresh(db_logement)

    return {
        "message": "Logement modifié avec succès",
        "logement": {
            "id_logement": db_logement.id_logement,
            "adresse_postale": db_logement.adresse_postale,
            "numero_telephone": db_logement.numero_telephone,
            "adresse_ip": db_logement.adresse_ip,
            "date_insertion": db_logement.date_insertion
        }
    }

# 🗑️ Supprimer un logement
@app.delete("/api/logements/{logement_id}")
def delete_logement(logement_id: int, session: Session = Depends(get_session)):
    logement = session.get(Logement, logement_id)
    if not logement:
        raise HTTPException(status_code=404, detail="Logement non trouvé")
    session.delete(logement)
    session.commit()
    return {"success": True}

# Route pour ajouter une pièce
@app.post("/api/pieces/")
def ajouter_piece(piece: Piece, session: Session = Depends(get_session)):
    session.add(piece)
    session.commit()
    session.refresh(piece)
    return {"message": "Pièce ajoutée avec succès", "id_piece": piece.id_piece}


@app.get("/api/pieces")
def get_pieces(session: Session = Depends(get_session), logement_id: Optional[int] = None):
    query = select(Piece)
    if logement_id:
        query = query.where(Piece.id_logement == logement_id)
    pieces = session.exec(query).all()
    return pieces

# Route pour ajouter un capteur/actionneur
@app.post("/api/capteur_actionneur/")
def ajouter_capteur_actionneur(capteur: Capteur_Actionneur, session: Session = Depends(get_session)):
    if not capteur.reference_commerciale:
        raise HTTPException(status_code=400, detail="La référence commerciale est requise.")

    session.add(capteur)
    session.commit()
    session.refresh(capteur)
    return capteur

@app.get("/api/capteurs_actionneurs")
def get_capteurs(session: Session = Depends(get_session), piece_id: Optional[int] = None):
    query = select(Capteur_Actionneur)
    if piece_id:
        query = query.where(Capteur_Actionneur.reference_piece == piece_id)
    capteurs = session.exec(query).all()
    return capteurs

@app.get("/api/types_capteurs_actionneurs/")
def read_types_capteurs_actionneurs(session: Session = Depends(get_session)):
    types_capteurs_actionneurs = session.exec(select(Type_Capteur_Actionneur)).all()
    return [{"id_type_capteur_actionneur": t.id_type_capteur_actionneur, "nom_type": t.nom_type} for t in types_capteurs_actionneurs]


@app.put("/api/pieces/{id_piece}")
def modifier_piece(id_piece: int, piece: Piece, session: Session = Depends(get_session)):
    db_piece = session.get(Piece, id_piece)
    if not db_piece:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    
    db_piece.nom = piece.nom or db_piece.nom
    db_piece.coord_x = piece.coord_x or db_piece.coord_x
    db_piece.coord_y = piece.coord_y or db_piece.coord_y
    db_piece.coord_z = piece.coord_z or db_piece.coord_z
    
    session.commit()
    session.refresh(db_piece)
    return db_piece


@app.delete("/api/pieces/{id_piece}")
def supprimer_piece(id_piece: int, session: Session = Depends(get_session)):
    db_piece = session.get(Piece, id_piece)
    if not db_piece:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    
    session.delete(db_piece)
    session.commit()
    return {"message": "Pièce supprimée avec succès"}





























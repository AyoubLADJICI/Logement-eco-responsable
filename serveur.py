from typing import Annotated,Optional, List
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
import pandas as pd
from retry_requests import retry
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from fastapi.staticfiles import StaticFiles
import matplotlib.dates as mdates
from datetime import datetime, timedelta 

# Configuration des templates
templates = Jinja2Templates(directory="templates")

# Modèles de données SQLModel
class Logement(SQLModel, table=True):
    id_logement : int = Field(default = None, primary_key = True)
    adresse_postale : str = Field(index=True)
    numero_telephone : str = Field(index=True)
    adresse_ip : str = Field(index=True)
    date_insertion: Optional[str] = Field(default="CURRENT_TIMESTAMP", nullable=False)

class Piece(SQLModel, table=True):
    id_piece : int = Field(default = None, primary_key = True)
    nom : str = Field(index=True)
    x : int = Field(index=True)
    y : int = Field(index=True)
    z : int = Field(index=True)
    id_logement : int = Field(index=True) 

class Capteur_Actionneur(SQLModel, table=True):
    id_capteur_actionneur : int = Field(default = None, primary_key = True)
    id_type : int = Field(index=True)
    nom : str = Field(index=True)
    reference_commerciale : str = Field(index=True)
    reference_piece : int = Field(index=True)
    port_communication : str = Field(index=True)
    date_insertion: Optional[str] = Field(default="CURRENT_TIMESTAMP", nullable=False)

class Type_Capteur_Actionneur(SQLModel, table=True):
    id_type_capteur_actionneur : int = Field(default = None, primary_key = True)
    nom_type : str = Field(index=True)
    unite : str = Field(index=True)
    min_valeur : float = Field(index=True)
    max_valeur : float = Field(index=True)
 
class Mesure(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_capteur_actionneur: int
    valeur: float
    date_insertion: Optional[str] = Field(default="CURRENT_TIMESTAMP", nullable=False)

class Facture(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_logement: int = Field(index=True)
    type_facture: str = Field(index=True)
    date_facture: Optional[str] = Field(default="CURRENT_TIMESTAMP", nullable=False)
    montant: float = Field(index=True)
    valeur_consommation: float = Field(index=True)

# Creation de notre moteur SQLModel 
# pour permettre a notre code de se connecter a notre base de donnees
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread" : False}
engine = create_engine(sqlite_url, connect_args=connect_args)    

# Fonction permettant de creer les tables pour
# tous les modeles de table dans notre BDD
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Fonction permettant de stocker ls objets en memoire
# Utilise le moteur pour communiquer avec la BDD
def get_session():
    with Session(engine) as session:
        yield session #Garantit une seule session pour chaque requete

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# Creation des tables de la BDD au demarrage de l'application
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#Chaque modele SQLModel est un modele Pydantic
#ce qui facilite la conversion des données entre
#les formats json et Python
@app.post("/logement/")
def create_logement(logement: Logement, session: SessionDep):
    session.add(logement)
    session.commit()
    session.refresh(logement)
    return logement

#Fonction permettant de lire les logements de la base de données
#a l'aide de la fonction select
@app.get("/logements/")
def read_logement(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)]=100,):
    logements = session.exec(select(Logement).offset(offset).limit(limit)).all()
    return logements

@app.get("/logements/{id_logement}")
def read_logement(id_logement: int, session: SessionDep):
    logement = session.get(Logement, id_logement)
    if not logement:
        raise HTTPException(status_code=404, detail="Logement not found")
    return logement

@app.delete("/logements/{logement_id}")
def delete_logement(id_logement: int, session: SessionDep):
    logement = session.get(Logement, id_logement)
    if not logement:
        raise HTTPException(status_code=404, detail="Logement Not Found")
    session.delete(logement)
    session.commit()
    return {"ok": True}

# Endpoints pour Piece
@app.post("/piece/")
def create_piece(piece: Piece, session: SessionDep):
    session.add(piece)
    session.commit()
    session.refresh(piece)
    return piece

@app.get("/pieces/")
def read_pieces(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    pieces = session.exec(select(Piece).offset(offset).limit(limit)).all()
    return pieces

@app.get("/pieces/{id_piece}")
def read_piece(id_piece: int, session: SessionDep):
    piece = session.get(Piece, id_piece)
    if not piece:
        raise HTTPException(status_code=404, detail="Piece not found")
    return piece

@app.delete("/pieces/{id_piece}")
def delete_piece(id_piece: int, session: SessionDep):
    piece = session.get(Piece, id_piece)
    if not piece:
        raise HTTPException(status_code=404, detail="Piece not found")
    session.delete(piece)
    session.commit()
    return {"ok": True}

# Endpoints pour Capteur_Actionneur
@app.post("/capteur_actionneur/")
def create_capteur_actionneur(capteur_actionneur: Capteur_Actionneur, session: SessionDep):
    session.add(capteur_actionneur)
    session.commit()
    session.refresh(capteur_actionneur)
    return capteur_actionneur

@app.get("/capteurs_actionneurs/")
def read_capteurs_actionneurs(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    capteurs_actionneurs = session.exec(select(Capteur_Actionneur).offset(offset).limit(limit)).all()
    return capteurs_actionneurs

@app.get("/capteurs_actionneurs/{id_capteur_actionneur}")
def read_capteur_actionneur(id_capteur_actionneur: int, session: SessionDep):
    capteur_actionneur = session.get(Capteur_Actionneur, id_capteur_actionneur)
    if not capteur_actionneur:
        raise HTTPException(status_code=404, detail="Capteur/Actionneur not found")
    return capteur_actionneur

@app.delete("/capteurs_actionneurs/{id_capteur_actionneur}")
def delete_capteur_actionneur(id_capteur_actionneur: int, session: SessionDep):
    capteur_actionneur = session.get(Capteur_Actionneur, id_capteur_actionneur)
    if not capteur_actionneur:
        raise HTTPException(status_code=404, detail="Capteur/Actionneur not found")
    session.delete(capteur_actionneur)
    session.commit()
    return {"ok": True}

# Endpoints pour Type_Capteur_Actionneur
@app.post("/type_capteur_actionneur/")
def create_type_capteur_actionneur(type_capteur_actionneur: Type_Capteur_Actionneur, session: SessionDep):
    session.add(type_capteur_actionneur)
    session.commit()
    session.refresh(type_capteur_actionneur)
    return type_capteur_actionneur

@app.get("/types_capteurs_actionneurs/")
def read_types_capteurs_actionneurs(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    types_capteurs_actionneurs = session.exec(select(Type_Capteur_Actionneur).offset(offset).limit(limit)).all()
    return types_capteurs_actionneurs

@app.get("/types_capteurs_actionneurs/{id_type_capteur_actionneur}")
def read_type_capteur_actionneur(id_type_capteur_actionneur: int, session: SessionDep):
    type_capteur_actionneur = session.get(Type_Capteur_Actionneur, id_type_capteur_actionneur)
    if not type_capteur_actionneur:
        raise HTTPException(status_code=404, detail="Type Capteur/Actionneur not found")
    return type_capteur_actionneur

@app.delete("/types_capteurs_actionneurs/{id_type_capteur_actionneur}")
def delete_type_capteur_actionneur(id_type_capteur_actionneur: int, session: SessionDep):
    type_capteur_actionneur = session.get(Type_Capteur_Actionneur, id_type_capteur_actionneur)
    if not type_capteur_actionneur:
        raise HTTPException(status_code=404, detail="Type Capteur/Actionneur not found")
    session.delete(type_capteur_actionneur)
    session.commit()
    return {"ok": True}


# Endpoints pour Mesure
@app.post("/mesures/")
def create_mesure(mesure: Mesure, session: SessionDep):
    session.add(mesure)
    session.commit()
    session.refresh(mesure)
    return mesure

@app.get("/mesures/")
def read_mesures(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    mesures = session.exec(select(Mesure).offset(offset).limit(limit)).all()
    return mesures

@app.delete("/mesures/{id}")
def delete_mesure(id: int, session: SessionDep):
    mesure = session.get(Mesure, id)
    if not mesure:
        raise HTTPException(status_code=404, detail="Mesure not found")
    session.delete(mesure)
    session.commit()
    return {"ok": True}

# Endpoints pour Facture
@app.post("/factures/")
def create_facture(facture: Facture, session: SessionDep):
    session.add(facture)
    session.commit()
    session.refresh(facture)
    return facture

@app.get("/factures/")
def read_factures(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    factures = session.exec(select(Facture).offset(offset).limit(limit)).all()
    return factures

@app.delete("/factures/{id}")
def delete_facture(id: int, session: SessionDep):
    facture = session.get(Facture, id)
    if not facture:
        raise HTTPException(status_code=404, detail="Facture not found")
    session.delete(facture)
    session.commit()
    return {"ok": True}

@app.get("/factures/chart", response_class=HTMLResponse)
async def chart_factures(request: Request, session: SessionDep):
    # Récupération de toutes les factures
    factures = session.exec(select(Facture)).all()

    # Regrouper par type et sommer les montants
    totals = {}
    for facture in factures:
        totals[facture.type_facture] = totals.get(facture.type_facture, 0) + facture.montant

    # Préparer les données pour Google Charts
    data = [["Type de Facture", "Montant Total"]]
    for type_facture, total in totals.items():
        data.append([type_facture, total])

    return templates.TemplateResponse("chart.html", {"request": request, "data": data})

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

    
@app.get("/openmeteo/{latitude}/{longitude}/page", response_class=HTMLResponse)
def display_open_meteo_weather(latitude: float, longitude: float, request: Request):
    try:
        data = fetch_open_meteo_weather(latitude, longitude)
        return templates.TemplateResponse(
            "meteo.html", {"request": request, "data": data.to_dict(orient="records")}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@app.get("/openmeteo/{latitude}/{longitude}/graph", response_class=HTMLResponse)
def display_weather_graph_separate(latitude: float, longitude: float):
    try:
        # Récupérer les données météo
        data = fetch_open_meteo_weather(latitude, longitude)

        # Convertir les dates
        dates = pd.to_datetime(data["date"])
        temperatures = data["temperature_2m"]
        humidity = data["relative_humidity_2m"]
        rain = data["rain"]

        # Création du premier graphique : Températures et Humidité
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(dates, temperatures, label="Température (°C)", color="red", linewidth=2)
        ax1.plot(dates, humidity, label="Humidité Relative (%)", color="blue", linestyle="--")
        ax1.set_title("Température et Humidité Relative", fontsize=16)
        ax1.set_xlabel("Date", fontsize=12)
        ax1.set_ylabel("Valeurs", fontsize=12)
        ax1.legend(loc="upper right", fontsize=10)
        ax1.tick_params(axis="x", rotation=45)
        plt.tight_layout()

        # Sauvegarder le premier graphique dans un buffer
        buf1 = BytesIO()
        plt.savefig(buf1, format="png")
        buf1.seek(0)
        image_base64_1 = base64.b64encode(buf1.read()).decode("utf-8")
        buf1.close()

        # Création du deuxième graphique : Précipitations
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.bar(dates, rain, color="gray", label="Pluie (mm)", alpha=0.6)
        ax2.set_title("Précipitations", fontsize=16)
        ax2.set_xlabel("Date", fontsize=12)
        ax2.set_ylabel("Précipitations (mm)", fontsize=12)
        ax2.legend(loc="upper right", fontsize=10)
        ax2.tick_params(axis="x", rotation=45)
        plt.tight_layout()

        # Sauvegarder le deuxième graphique dans un buffer
        buf2 = BytesIO()
        plt.savefig(buf2, format="png")
        buf2.seek(0)
        image_base64_2 = base64.b64encode(buf2.read()).decode("utf-8")
        buf2.close()

        # Retourner les deux graphiques dans une page HTML
        return f"""
        <html>
            <body>
                <center><h1>Graphiques des Prévisions Météo</h1></center>
                <center><h2>Température et Humidité Relative</h2></center>
                <center><img src="data:image/png;base64,{image_base64_1}" /></center>
                <center><h2>Précipitations</h2></center>
                <center><img src="data:image/png;base64,{image_base64_2}" /></center>
            </body>
        </html>
        """
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération des graphiques : {str(e)}")
    
@app.post("/capteurs/temperature")
def receive_temperature(data: dict, session: SessionDep):
    """
    Reçoit une température depuis l'ESP8266 et prend une décision.
    """
    # Extraction de la température envoyée
    temperature = data.get("temperature")
    if temperature is None:
        raise HTTPException(status_code=400, detail="Donnée 'temperature' manquante.")

    # Enregistrement dans la table `Mesure`
    mesure = Mesure(
        id_capteur_actionneur=1,  # ID du capteur de température, à adapter si nécessaire
        valeur=temperature
    )
    session.add(mesure)
    session.commit()

    # Logique de déclenchement de l'action en fonction du seuil
    seuil_temperature = 25.0  # Seuil pour la température
    if temperature > seuil_temperature:
        action = "LED_ON"
        print(f"Température {temperature}°C détectée, action : {action}")
    else:
        action = "LED_OFF"
        print(f"Température {temperature}°C détectée, action : {action}")

    # Retourner l'action au client (ESP)
    return {"action": action, "temperature": temperature}

# Configurer les fichiers statiques
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes pour servir les pages HTML
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
def get_statistics(session: SessionDep):
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

@app.get("/api/consommation")
def get_consumption_data(session: SessionDep, logement_id: Optional[int] = None):
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



@app.get("/api/logements")
def get_logements(session: SessionDep):
    logements = session.exec(select(Logement)).all()
    return [{"id_logement": logement.id_logement, "adresse": logement.adresse_postale} for logement in logements]


@app.get("/api/pieces_capteurs")
def get_pieces_capteurs(logement_id: int, session: SessionDep):
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
                    "etat": capteur.port_communication  # Associe un état factice "ON/OFF" pour simplifier
                }
                for capteur in capteurs
            ]
        })
    return result

@app.post("/api/capteur_toggle/{capteur_id}")
def toggle_capteur(capteur_id: int, session: SessionDep):
    capteur = session.get(Capteur_Actionneur, capteur_id)
    if not capteur:
        raise HTTPException(status_code=404, detail="Capteur non trouvé")

    # Basculer l'état fictif "ON/OFF"
    if capteur.port_communication == "ON":
        capteur.port_communication = "OFF"
    else:
        capteur.port_communication = "ON"

    session.add(capteur)
    session.commit()
    session.refresh(capteur)

    return {"success": True, "etat": capteur.port_communication}






#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

// Configuration Wi-Fi
const char* ssid = "Xiaomi";
const char* password = "12345678";
const char* serverUrl = "http://192.168.72.223:8000/capteurs/temperature"; // Remplace par l'adresse de ton serveur

// Configuration DHT
#define DHTPIN D0 // Pin où le DHT est connecté
#define DHTTYPE DHT11 // DHT11 ou DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  // Connexion au Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connexion au Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnecté au Wi-Fi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    float temperature = dht.readTemperature();

    // Vérifier si la valeur est valide
    if (isnan(temperature)) {
      Serial.println("Erreur lors de la lecture du DHT !");
      return;
    }

    // Envoyer la température au serveur
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    // Format JSON pour l'envoi
    String jsonData = "{\"id_capteur_actionneur\": 1, \"valeur\": " + String(temperature, 2) + "}";
    int httpCode = http.POST(jsonData);

    if (httpCode > 0) {
      Serial.println("Température envoyée avec succès !");
    } else {
      Serial.println("Erreur lors de l'envoi de la température");
    }

    http.end();
  } else {
    Serial.println("Wi-Fi déconnecté");
  }

  delay(10000); // Envoi toutes les 10 secondes
}
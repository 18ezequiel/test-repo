import requests
import pandas as pd
import json

# Configura la URL base para la API de Google Places
places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Configura los parámetros de la búsqueda
params = {
    "location": "40.69313,-73.57546", # coordenadas de Nueva York
    "radius": 38224, # radio de búsqueda en metros
    "type": "restaurant", # tipo de lugar a buscar
    "region" : "NY",
    "key": "AIzaSyB2v7bruAooTsZ1Xj_B022vn9I4F3SeDMQ", # clave de API de Google Maps
    "fields": "name,geometry,types,place_id,user_ratings_total,url",
    "keyword": "restaurant",
}

# Realiza la solicitud a la API de Places de Google Maps
response = requests.get(places_url, params=params)

if response.status_code == 200:
    # Si la respuesta es correcta, procesa la información
    results = response.json()["results"]
    data = {"places": []}  # Crea un diccionario para guardar los datos
    for result in results:
        # Agrega cada registro como un elemento de lista en el diccionario
        place = {
            "name": result["name"],
            "coordinates": result["geometry"]["location"],
            "categories": result["types"],
            "gmap_id": result["place_id"],
            "url": f"https://www.google.com/maps/place/?q=place_id:{result['place_id']}",
            "total_ratings": result["user_ratings_total"],
            "delivery": "Sí" if "delivery" in result.get("business_status", "") else "No",
            "takeout": "Sí" if "takeout" in result.get("business_status", "") else "No",
        }
        data["places"].append(place)

        # Imprime la información del lugar
        print("Lugar:", place["name"])
        print("Coordenadas:", place["coordinates"])
        print("Categorías:", place["categories"])
        print("GMap ID:", place["gmap_id"])
        print("URL:", place["url"])
        print("Total de ratings:", place["total_ratings"])
        print("Delivery:", place["delivery"])
        print("Takeout:", place["takeout"])

    # Escribe el diccionario en un archivo JSON
    with open("data.json", "w") as f:
        json.dump(data, f)
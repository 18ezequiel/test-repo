import requests
import pandas as pd

# Configura la URL base para la API de Google Places
places_url = "https://maps.googleapis.com/maps/api/place/details/json"

# Configura los parámetros de la búsqueda
params = {
    "place_id": "ChIJH97jp3b2wokRyoBwNMM-F9U", # place_id
    "type": "restaurant", # tipo de lugar a buscar
    "region" : "NY",
    "key": "AIzaSyB2v7bruAooTsZ1Xj_B022vn9I4F3SeDMQ", # clave de API de Google Maps
    "fields": "name,geometry,types,place_id,url,delivery,takeout,serves_breakfast,serves_dinner,serves_lunch",
    "keyword": "restaurant",
}

# Realiza la solicitud a la API de Places de Google Maps
response = requests.get(places_url, params=params)

# Obtén los datos del diccionario de la respuesta de la API
data = response.json()["result"]

# Crea un diccionario con los datos
df_dict = {
    "Lugar": data["name"],
    "Coordenadas": f'{data["geometry"]["location"]["lat"]}, {data["geometry"]["location"]["lng"]}',
    "Categorías": ", ".join(data["types"]),
    "GMap ID": data["place_id"],
    "URL": f"https://www.google.com/maps/place/?q=place_id:{data['place_id']}",
    "Delivery": str(data.get("delivery", False)),
    "Takeout": str(data.get("takeout", False)),
    "Serves Breakfast": str(data.get("serves_breakfast", False)),
    "Serves Lunch": str(data.get("serves_lunch", False)),
    "Serves Dinner": str(data.get("serves_dinner", False))
}

# Crea el DataFrame
df = pd.DataFrame(df_dict, index=[0])

print(df)


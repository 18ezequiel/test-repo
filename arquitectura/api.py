import requests
import pandas as pd


# Configura la URL base para la API de Google Places
places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Configura los parámetros de la búsqueda
params = {
    "location": "40.69313,-73.57546", # coordenadas de Nueva York
    "radius": 38224, # radio de búsqueda en metros
    "type": "restaurant", # tipo de lugar a buscar
    "region" : "NY",
    "key": "AIzaSyB2v7bruAooTsZ1Xj_B022vn9I4F3SeDMQ", # clave de API de Google Maps
    "fields": "place_id",
    "keyword": "restaurant",
}

# Realiza la solicitud a la API de Places de Google Maps
response = requests.get(places_url, params=params)

if response.status_code == 200:
    # Si la respuesta es correcta, procesa la información
    results = response.json()["results"]
    #print(results)
    lista_place_id=[]
    for result in results:
        lista_place_id.append(result["place_id"])




contador = 0
for place_id in lista_place_id:
    # Configura la URL base para la API de Google Places
    places_url = "https://maps.googleapis.com/maps/api/place/details/json"

    # Configura los parámetros de la búsqueda
    params = {
        "place_id": place_id, # place_id
        "type": "restaurant", # tipo de lugar a buscar
        "region" : "NY",
        "key": "AIzaSyB2v7bruAooTsZ1Xj_B022vn9I4F3SeDMQ", # clave de API de Google Maps
        "fields": "name,geometry,rating,adr_address,types,place_id,url,delivery,takeout,serves_breakfast,serves_dinner,serves_lunch",
        "keyword": "restaurant",
    }

    # Realiza la solicitud a la API de Places de Google Maps
    response = requests.get(places_url, params=params)

    # Obtén los datos del diccionario de la respuesta de la API
    data = response.json()["result"]

    # Crea un diccionario con los datos
    df_dict = {
        "name": data["name"],
        "coordenada": f'{data["geometry"]["location"]["lat"]}, {data["geometry"]["location"]["lng"]}',
        "category": ", ".join(data["types"]),
        "gmap_id": data["place_id"],
        "address":data["adr_address"],
        "avg_rating": data['rating'],
        "url": f"https://www.google.com/maps/place/?q=place_id:{data['place_id']}",
        "delivery": str(data.get("delivery", False)),
        "takeout": str(data.get("takeout", False)),
        "serves_breakfast": str(data.get("serves_breakfast", False)),
        "serves_lunch": str(data.get("serves_lunch", False)),
        "serves_dinner": str(data.get("serves_dinner", False))
    }

    # Crea el DataFrame
    df = pd.DataFrame(df_dict, index=[0])

    if contador == 0:
        df_final = df
        contador+=1
        continue
    df_final = pd.concat([df_final, df])
    contador+=1

df_final = df_final.reset_index(drop=True)
df_final.drop_duplicates(inplace=True)
print(df_final.info())
df_final.to_json('salida_api_1.json', orient='records')
import requests
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()


API_KEY = os.getenv('OPENWEATHER_API_KEY')


BASE_URL = 'https://api.openweathermap.org/data/2.5'

villes = ['Tourcoing', 'Lille', 'Lomme', 'Roubaix','Loos','Englos','Lambersart','Comines','Leers','Roncq']


url = f'{BASE_URL}/weather'

meteo_data =[]
for ville in villes:
    params = {
        'q': ville,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }



    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        meteo_data.append({
            'Ville': ville,
            'Température (°C)': data['main']['temp'],
            'Ressenti (°C)': data['main']['feels_like'],
            'Humidité (%)': data['main']['humidity'],
            'Description': data['weather'][0]['description']
        })
    else:
        print(f"Erreur pour {ville} : {response.status_code}")

    # . Pour chaque ville, récupérer :
    #    - Température actuelle
    #    - Température ressentie
    #    - Humidité
    #    - Description
    
#     print(data)

df_meteo = pd.DataFrame(meteo_data)

print(df_meteo)

# Créer un DataFrame avec ces informations

ville_plus_chaude = df_meteo.loc[df_meteo['Température (°C)'].idxmax()]
print(ville_plus_chaude)
ville_plus_froide = df_meteo.loc[df_meteo['Température (°C)'].idxmin()]
print(ville_plus_froide)

# 5. Calculer la température moyenne
moyenne_temp = df_meteo['Température (°C)'].mean().round(2)
print("La température moyenne : ", moyenne_temp)

# 6. Sauvegarder dans `meteo_villes.csv`
df_meteo.to_csv('meteo_villes_france.csv', index=False)

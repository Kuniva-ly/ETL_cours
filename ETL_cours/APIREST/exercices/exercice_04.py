import requests
import pandas as pd
from openpyxl import load_workbook


BASE_URL = "https://restcountries.com/v3.1"
users_url = f"{BASE_URL}/region/europe"
#Tous les pays

response = requests.get(users_url)
eu_pays = response.json()

print("Les pays d'europes :", eu_pays)



# 2. Créer un DataFrame avec : nom, capitale, population, superficie
country_eu = []
for country in eu_pays:
    country_name = country.get("name").get('common')
    country_capital = country.get("capital") 
    country_population = country.get('population')
    country_area = country.get('area')
    country_eu.append({
        'country_name': country_name,
        'country_capital': country_capital[0] if country_capital else None,
        'country_population': country_population,
        'country_area': country_area
    })
    
df_eu_country = pd.DataFrame(country_eu)


# 3. Calculer la densité de population (population / superficie)

df_eu_country['density'] = df_eu_country['country_population']/df_eu_country['country_area']
# print(df_eu_country)
# 4. Identifier les 5 pays les plus peuplés d'Europe
top_5_people = df_eu_country.nlargest(5, 'country_population')
print(f"Le top 5 des pays les plus peupler : {top_5_people}")

# 5. Calculer la population totale de l'Europe
population_totale = df_eu_country['country_population'].sum()
print(f"\nPopulation totale de l'Europe : {population_totale}")

# 6. Trouver le pays avec la plus grande densité

pays_densite_max = df_eu_country.nlargest(1, 'density')
print(f"\nPays avec la plus grande densité de population : {pays_densite_max}")

#  # 7. Sauvegarder les résultats dans `pays_europe.xlsx`

# workbook = load_workbook('pays_europe.xlsx')
# workbook.active = 0  
# workbook.save('pays_europe.xlsx')


 
with pd.ExcelWriter('Europe.xlsx') as writer:
    df_eu_country.to_excel(writer, sheet_name='Europe', index=False)
    
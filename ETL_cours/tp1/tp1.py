import pandas as pd


fichiers = ['magasin_A.csv', 'magasin_B.csv','magasin_C.csv']
df_final = []
for fichier in fichiers:
    fichier.split('_')[1].split('.csv')
    dataframe = pd.read_csv(fichier, sep=",")
    if "A" in fichier:
        dataframe["magasin"] = "A"
    elif "B" in fichier:
        dataframe["magasin"] = "B"
    elif "C" in fichier:
        dataframe["magasin"] = "C"
    df_final.append(df_final) 



# 1. Charger tous les fichiers CSV
# 2. Ajouter une colonne `magasin` (A, B ou C)
# 3. Concaténer tous les DataFrames
df_a = pd.read_csv('magasin_A.csv')
df_b = pd.read_csv('magasin_B.csv')
df_c = pd.read_csv('magasin_C.csv')

df_a['magasin'] = 'A'
df_b['magasin'] = 'B'
df_c['magasin'] = 'C'

df_final = pd.concat([df_a, df_b, df_c], ignore_index=True)  
# print(df_final)

#4. Nettoyer (doublons, valeurs manquantes)
df_final.drop_duplicates()
df_final.dropna()
print(df_final.isnull().sum())

#5. Calculer `montant_total`
df_final["montant_total"] = df_final["quantite"] * df_final["prix_unitaire"]

# 6. Créer un rapport Excel avec :
#    - Feuille "Consolidé" : Toutes les données
#    - Feuille "Par magasin" : Totaux par magasin
#    - Feuille "Par vendeur" : Performance des vendeurs
#    - Feuille "Top produits" : 10 produits les plus vendus

total_ventes_par_magasin = df_final.groupby('magasin', as_index=False)['montant_total'].sum()
total_ventes_par_vendeur = df_final.groupby('vendeur', as_index=False)['montant_total'].sum()
par_produit = df_final.groupby('produit', as_index=False)['montant_total'].sum()
par_produit = par_produit.sort_values('montant_total',ascending=False)
top10_produit = par_produit.head(10)

with pd.ExcelWriter('rapport_tp.xlsx' ,engine='openpyxl') as writer:
    df_final.to_excel(writer, sheet_name='Données', index=False)
    total_ventes_par_magasin.to_excel(writer, sheet_name='Par magasin', index=False)
    total_ventes_par_vendeur.to_excel(writer, sheet_name='Par vendeur', index=False) 
    top10_produit.to_excel(writer, sheet_name='Top 10 produits', index=False)  
import pandas as pd



# 1
df =  pd.read_excel('ventes_janvier.xlsx')

# 2. Nettoyer :
#    - Supprimer les doublons
df.drop_duplicates()
#    - Remplir les valeurs manquantes de `region` par "Non spécifié"
df['region'].fillna("Non spécifié", inplace=True)
#    - Convertir `date` en datetime
df['date'] = pd.to_datetime(df['date'])

# 3. Transformer :
#    - Créer `montant_total` = quantite × prix_unitaire
df["montant_total"] = df["quantite"] * df["prix_unitaire"]
#    - Extraire le `jour` et `jour_semaine` de la date
df['jour_semaine'] = df['date'].dt.dayofweek
df['nom_jour'] = df['date'].dt.day_name(locale='fr_FR.UTF-8')
print(df['nom_jour'])

# 4. Analyser :
#    - Total des ventes par région
total_ventes_par_region = df.groupby('region', as_index=False)['montant_total'].sum()
print(total_ventes_par_region)
#    - Produit le plus vendu (en quantité)
top1 = df.nlargest(1,'montant_total')[['produit','montant_total']]
print(top1)
#    - Jour de la semaine avec le plus de ventes

top_day = df[['nom_jour', 'produit', 'montant_total']].nlargest(1, 'montant_total')
print(top_day) 

# 5. Créer un fichier Excel avec 3 feuilles :
#    - Feuille "Données" : Données nettoyées
#    - Feuille "Par région" : Agrégation par région
#    - Feuille "Par produit" : Agrégation par produit
df_par_produit = df.groupby('produit', as_index=False)['montant_total'].sum()
# Agrégations nécessaires


# Écriture dans un fichier Excel avec 3 feuilles
with pd.ExcelWriter('rapport.xlsx') as writer:
    df.to_excel(writer, sheet_name='Données', index=False)
    total_ventes_par_region.to_excel(writer, sheet_name='Par région', index=False)
    df_par_produit.to_excel(writer, sheet_name='Par produit', index=False)   
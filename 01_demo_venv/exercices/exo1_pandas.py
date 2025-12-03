import pandas as pd

# data = {
#     "date": ["2024-01-15", "2024-01-15", "2024-01-16", "2024-01-16", "2024-01-17"],
#     "produit": ["Laptop", "Souris", "Clavier", "Laptop", "Souris"],
#     "quantite": [2, 5, 3, 1, 10],
#     "prix_unitaire": [899.99, 29.99, 79.99, 899.99, 29.99],
#     "vendeur": ["Alice", "Bob", "Alice", "Charlie", "Alice"]
# }


df = pd.read_csv('ventes.csv')
# df.head()

df["montant_total"] = df["quantite"] * df["prix_unitaire"]
# print(df)

# total_ventes_par_vendeur = df.groupby("vendeur")["montant_total"].sum()   
# print(total_ventes_par_vendeur)

# #4
# total_ventes_par_produit = df.groupby("produit")["montant_total"].sum() 
# print(total_ventes_par_produit)


# #5
# top_3 = df.groupby("produit")["montant_total"].sum().sort_values(ascending=False)  
# print(total_ventes_par_produit)
# print(df.head(3))

# #6
# df.to_csv("ventes_analysees.csv", index=False)
# print(df.nlargest(3 ,"montant_total"))

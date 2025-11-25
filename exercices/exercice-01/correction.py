"""
CORRECTION DE L'EXERCICE 01
Accès protégé par mot de passe
"""

import getpass

def verifier_mot_de_passe():
    """Vérifie le mot de passe avant d'afficher la correction"""
    mot_de_passe = getpass.getpass("Entrez le mot de passe pour accéder à la correction : ")
    if mot_de_passe == "Abidexercice123":
        return True
    else:
        print("❌ Mot de passe incorrect. Accès refusé.")
        return False

if not verifier_mot_de_passe():
    exit()

print("\n" + "="*60)
print("CORRECTION DE L'EXERCICE 01 - MANIPULATION PANDAS")
print("="*60 + "\n")

# ============================================================================
# ÉTAPE 1 : CHARGEMENT DES DONNÉES
# ============================================================================

print("ÉTAPE 1 : Chargement des données\n")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Chargement
df = pd.read_csv('donnees/ventes.csv')

# Affichage des premières lignes
print("Premières lignes :")
print(df.head())
print("\n" + "-"*60 + "\n")

# Informations générales
print("Informations sur le DataFrame :")
print(df.info())
print("\n" + "-"*60 + "\n")

print("Statistiques descriptives :")
print(df.describe())
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 2 : NETTOYAGE DES DONNÉES
# ============================================================================

print("ÉTAPE 2 : Nettoyage des données\n")

# Vérification des valeurs manquantes
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("\n" + "-"*60 + "\n")

# Traitement des valeurs manquantes (si présentes)
# Dans ce cas, les données générées n'ont pas de valeurs manquantes
# Mais voici comment on le ferait :
# df = df.dropna()  # Supprimer les lignes avec valeurs manquantes
# ou
# df['colonne'] = df['colonne'].fillna(df['colonne'].mean())  # Remplacer par la moyenne

# Vérification des doublons
nb_doublons = df.duplicated().sum()
print(f"Nombre de doublons : {nb_doublons}")
if nb_doublons > 0:
    df = df.drop_duplicates()
    print("Doublons supprimés")
print("\n" + "-"*60 + "\n")

# Conversion de la colonne date
df['date'] = pd.to_datetime(df['date'])
print("Colonne date convertie en datetime")
print(f"Type : {df['date'].dtype}")
print("\n" + "-"*60 + "\n")

# Vérification des types
print("Types de données :")
print(df.dtypes)
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 3 : ANALYSE EXPLORATOIRE
# ============================================================================

print("ÉTAPE 3 : Analyse exploratoire\n")

# Statistiques descriptives
print("Statistiques sur les quantités :")
print(df['quantite'].describe())
print("\n" + "-"*60 + "\n")

print("Statistiques sur les prix :")
print(df['prix_unitaire'].describe())
print("\n" + "-"*60 + "\n")

# Calcul du chiffre d'affaires par produit
df['ca'] = df['quantite'] * df['prix_unitaire']

# Top 10 produits par CA
top_produits = df.groupby('produit')['ca'].sum().sort_values(ascending=False).head(10)
print("Top 10 produits par chiffre d'affaires :")
print(top_produits)
print("\n" + "-"*60 + "\n")

# CA par mois
df['mois'] = df['date'].dt.to_period('M')
ca_par_mois = df.groupby('mois')['ca'].sum().sort_values(ascending=False)
print("Chiffre d'affaires par mois :")
print(ca_par_mois)
print("\n" + "-"*60 + "\n")

# Mois avec le plus de ventes
mois_max = ca_par_mois.idxmax()
ca_max = ca_par_mois.max()
print(f"Mois avec le plus de ventes : {mois_max}")
print(f"Chiffre d'affaires : {ca_max:,.2f} €")
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 4 : VISUALISATION
# ============================================================================

print("ÉTAPE 4 : Création des visualisations\n")

# Graphique 1 : CA par mois
plt.figure(figsize=(12, 6))
ca_par_mois.plot(kind='bar', color='steelblue')
plt.title('Chiffre d\'affaires par mois', fontsize=16, fontweight='bold')
plt.xlabel('Mois', fontsize=12)
plt.ylabel('Chiffre d\'affaires (€)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('correction_graphique_ventes_mois.png', dpi=300, bbox_inches='tight')
print("✅ Graphique CA par mois sauvegardé : correction_graphique_ventes_mois.png")
plt.close()

# Graphique 2 : Répartition par catégorie
ca_par_categorie = df.groupby('categorie')['ca'].sum()
plt.figure(figsize=(10, 8))
plt.pie(ca_par_categorie, labels=ca_par_categorie.index, autopct='%1.1f%%', 
        startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Répartition du chiffre d\'affaires par catégorie', 
          fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('correction_graphique_categories.png', dpi=300, bbox_inches='tight')
print("✅ Graphique catégories sauvegardé : correction_graphique_categories.png")
plt.close()

print("\n" + "-"*60 + "\n")

# ============================================================================
# RÉSUMÉ
# ============================================================================

print("RÉSUMÉ DE L'ANALYSE\n")

print(f"Nombre total de transactions : {len(df)}")
print(f"Période analysée : {df['date'].min().strftime('%Y-%m-%d')} à {df['date'].max().strftime('%Y-%m-%d')}")
print(f"Chiffre d'affaires total : {df['ca'].sum():,.2f} €")
print(f"Nombre de produits différents : {df['produit'].nunique()}")
print(f"Nombre de clients différents : {df['client_id'].nunique()}")
print(f"\nTop catégorie : {df.groupby('categorie')['ca'].sum().idxmax()}")
print(f"CA de la top catégorie : {df.groupby('categorie')['ca'].sum().max():,.2f} €")

print("\n" + "="*60)
print("FIN DE LA CORRECTION")
print("="*60)


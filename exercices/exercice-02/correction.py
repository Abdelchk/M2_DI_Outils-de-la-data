"""
CORRECTION DE L'EXERCICE 02 - ANALYSE SQL
Accès protégé par mot de passe
"""

import getpass
import sqlite3
import pandas as pd

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
print("CORRECTION DE L'EXERCICE 02 - ANALYSE SQL")
print("="*60 + "\n")

# Connexion à la base de données
conn = sqlite3.connect('donnees/boutique.db')

# ============================================================================
# ÉTAPE 1 : EXPLORATION
# ============================================================================

print("ÉTAPE 1 : Exploration de la base de données\n")

# Liste des tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("Tables disponibles :")
print(tables)
print("\n" + "-"*60 + "\n")

# Structure et nombre d'enregistrements
for table in ['clients', 'produits', 'commandes', 'details_commandes']:
    print(f"Table : {table}")
    df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 5", conn)
    print(f"Structure : {list(df.columns)}")
    count = pd.read_sql_query(f"SELECT COUNT(*) as count FROM {table}", conn)
    print(f"Nombre d'enregistrements : {count['count'].iloc[0]}")
    print()

print("-"*60 + "\n")

# ============================================================================
# ÉTAPE 2 : REQUÊTES DE BASE
# ============================================================================

print("ÉTAPE 2 : Requêtes de base\n")

# Sélection simple
print("1. Tous les clients :")
df = pd.read_sql_query("SELECT nom, prenom, email FROM clients", conn)
print(df.head())
print()

# Filtrage
print("2. Produits > 100€ :")
df = pd.read_sql_query("SELECT * FROM produits WHERE prix > 100", conn)
print(df)
print()

# Tri
print("3. Commandes triées par date :")
df = pd.read_sql_query("SELECT * FROM commandes ORDER BY date_commande DESC", conn)
print(df.head())
print()

# Limite
print("4. Top 5 produits les plus chers :")
df = pd.read_sql_query("SELECT * FROM produits ORDER BY prix DESC LIMIT 5", conn)
print(df)
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 3 : AGRÉGATION
# ============================================================================

print("ÉTAPE 3 : Requêtes avec agrégation\n")

# Nombre total de commandes
nb_commandes = pd.read_sql_query("SELECT COUNT(*) as total FROM commandes", conn)
print(f"Nombre total de commandes : {nb_commandes['total'].iloc[0]}")
print()

# Montant total
montant_total = pd.read_sql_query("SELECT SUM(montant_total) as total FROM commandes", conn)
print(f"Montant total : {montant_total['total'].iloc[0]:.2f} €")
print()

# Panier moyen
panier_moyen = pd.read_sql_query("SELECT AVG(montant_total) as moyen FROM commandes", conn)
print(f"Panier moyen : {panier_moyen['moyen'].iloc[0]:.2f} €")
print()

# Commandes par client
print("Nombre de commandes par client :")
df = pd.read_sql_query("""
    SELECT c.client_id, c.nom, c.prenom, COUNT(co.commande_id) as nb_commandes
    FROM clients c
    LEFT JOIN commandes co ON c.client_id = co.client_id
    GROUP BY c.client_id
    ORDER BY nb_commandes DESC
""", conn)
print(df)
print()

# Client qui a dépensé le plus
print("Client qui a dépensé le plus :")
df = pd.read_sql_query("""
    SELECT c.client_id, c.nom, c.prenom, SUM(co.montant_total) as total_depense
    FROM clients c
    JOIN commandes co ON c.client_id = co.client_id
    GROUP BY c.client_id
    ORDER BY total_depense DESC
    LIMIT 1
""", conn)
print(df)
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 4 : JOINTURES
# ============================================================================

print("ÉTAPE 4 : Jointures\n")

# Commandes avec noms clients
print("Commandes avec noms des clients :")
df = pd.read_sql_query("""
    SELECT co.commande_id, co.date_commande, co.montant_total,
           c.nom, c.prenom, c.email
    FROM commandes co
    JOIN clients c ON co.client_id = c.client_id
""", conn)
print(df.head())
print()

# Produits commandés avec détails
print("Produits commandés avec détails :")
df = pd.read_sql_query("""
    SELECT dc.commande_id, p.nom as produit, p.categorie, 
           dc.quantite, dc.prix_unitaire,
           (dc.quantite * dc.prix_unitaire) as montant
    FROM details_commandes dc
    JOIN produits p ON dc.produit_id = p.produit_id
    ORDER BY dc.commande_id
""", conn)
print(df.head(10))
print()

# CA par client
print("Chiffre d'affaires par client :")
df = pd.read_sql_query("""
    SELECT c.client_id, c.nom, c.prenom, 
           SUM(co.montant_total) as ca_total
    FROM clients c
    JOIN commandes co ON c.client_id = co.client_id
    GROUP BY c.client_id
    ORDER BY ca_total DESC
""", conn)
print(df)
print()

# Produits les plus vendus
print("Produits les plus vendus (quantité) :")
df = pd.read_sql_query("""
    SELECT p.nom, p.categorie, SUM(dc.quantite) as quantite_totale
    FROM details_commandes dc
    JOIN produits p ON dc.produit_id = p.produit_id
    GROUP BY p.produit_id
    ORDER BY quantite_totale DESC
""", conn)
print(df)
print("\n" + "-"*60 + "\n")

# ============================================================================
# ÉTAPE 5 : REQUÊTES COMPLEXES
# ============================================================================

print("ÉTAPE 5 : Requêtes complexes\n")

# Clients sans commande
print("Clients qui n'ont jamais passé de commande :")
df = pd.read_sql_query("""
    SELECT c.*
    FROM clients c
    LEFT JOIN commandes co ON c.client_id = co.client_id
    WHERE co.commande_id IS NULL
""", conn)
print(df)
print()

# CA par mois
print("Chiffre d'affaires par mois :")
df = pd.read_sql_query("""
    SELECT strftime('%Y-%m', date_commande) as mois,
           SUM(montant_total) as ca_mois
    FROM commandes
    GROUP BY mois
    ORDER BY mois
""", conn)
print(df)
print()

# Top 3 clients
print("Top 3 clients (CA) :")
df = pd.read_sql_query("""
    SELECT c.nom, c.prenom, SUM(co.montant_total) as ca_total
    FROM clients c
    JOIN commandes co ON c.client_id = co.client_id
    GROUP BY c.client_id
    ORDER BY ca_total DESC
    LIMIT 3
""", conn)
print(df)
print()

# Produits jamais commandés
print("Produits jamais commandés :")
df = pd.read_sql_query("""
    SELECT p.*
    FROM produits p
    LEFT JOIN details_commandes dc ON p.produit_id = dc.produit_id
    WHERE dc.detail_id IS NULL
""", conn)
print(df)
print()

# Panier moyen par catégorie
print("Panier moyen par catégorie :")
df = pd.read_sql_query("""
    SELECT p.categorie, 
           AVG(dc.quantite * dc.prix_unitaire) as panier_moyen
    FROM details_commandes dc
    JOIN produits p ON dc.produit_id = p.produit_id
    GROUP BY p.categorie
""", conn)
print(df)
print("\n" + "-"*60 + "\n")

conn.close()

print("="*60)
print("FIN DE LA CORRECTION")
print("="*60)


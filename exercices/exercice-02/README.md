# Exercice 02 : Analyse de données avec SQL

## 🎯 Objectifs

- Maîtriser les requêtes SQL de base et avancées
- Apprendre à joindre des tables
- Utiliser des fonctions d'agrégation
- Créer des vues et des requêtes complexes

## 📋 Prérequis

- Python 3.8+
- Bibliothèques : sqlite3 (incluse), pandas
- Connaissances de base en SQL

## 📦 Installation

```bash
pip install pandas
```

## 📊 Base de données

Une base de données SQLite est fournie dans `donnees/boutique.db` avec les tables suivantes :
- `clients` : Informations sur les clients
- `produits` : Catalogue des produits
- `commandes` : Historique des commandes
- `details_commandes` : Détails de chaque commande

## 🎓 Instructions

### Étape 1 : Exploration de la base de données

1. Créez un script Python `solution.py` dans votre dossier de solution
2. Connectez-vous à la base de données SQLite
3. Listez toutes les tables disponibles
4. Affichez la structure de chaque table (colonnes et types)
5. Comptez le nombre d'enregistrements dans chaque table

### Étape 2 : Requêtes de base

1. **Sélection simple** : Affichez tous les clients avec leur nom et email
2. **Filtrage** : Trouvez tous les produits dont le prix est supérieur à 100€
3. **Tri** : Listez les commandes triées par date (plus récentes en premier)
4. **Limite** : Affichez les 5 produits les plus chers

### Étape 3 : Requêtes avec agrégation

1. Calculez le nombre total de commandes
2. Calculez le montant total de toutes les commandes
3. Trouvez le panier moyen (montant moyen par commande)
4. Comptez le nombre de commandes par client
5. Trouvez le client qui a dépensé le plus

### Étape 4 : Jointures

1. Affichez toutes les commandes avec les noms des clients
2. Listez tous les produits commandés avec leurs détails (nom, prix, quantité)
3. Créez une vue qui montre le chiffre d'affaires par client avec leurs informations
4. Trouvez les produits les plus vendus (en quantité)

### Étape 5 : Requêtes complexes

1. Trouvez les clients qui n'ont jamais passé de commande
2. Calculez le chiffre d'affaires par mois
3. Identifiez les 3 meilleurs clients (en termes de CA)
4. Trouvez les produits qui n'ont jamais été commandés
5. Calculez le panier moyen par catégorie de produit

### Étape 6 : Export et analyse

1. Exportez les résultats des requêtes importantes en CSV
2. Créez un fichier `resultats.md` avec :
   - Un résumé de votre analyse
   - Les requêtes SQL utilisées (avec explications)
   - Les principales découvertes
   - Les statistiques clés

## 📁 Structure attendue

```
exercice-02/
├── README.md (ce fichier)
├── donnees/
│   └── boutique.db
└── solutions/
    └── votre-nom/
        ├── solution.py
        ├── resultats.md
        ├── ca_par_client.csv
        └── produits_populaires.csv
```

## ✅ Critères d'évaluation

- [ ] Toutes les requêtes fonctionnent correctement
- [ ] Code bien commenté et organisé
- [ ] Utilisation appropriée des jointures
- [ ] Les requêtes complexes sont optimisées
- [ ] Le fichier `resultats.md` est complet

## 💡 Conseils

- Utilisez `pd.read_sql_query()` pour exécuter des requêtes et obtenir des DataFrames
- Testez vos requêtes une par une avant de les intégrer dans le script
- Utilisez des alias de tables pour rendre les requêtes plus lisibles
- Documentez chaque requête avec un commentaire expliquant son objectif

## 📚 Ressources SQL

- Documentation SQLite : https://www.sqlite.org/docs.html
- Tutoriel SQL : https://www.w3schools.com/sql/

## 🆘 Aide

Si vous êtes bloqué :
1. Consultez la documentation SQLite
2. Ouvrez une issue sur le dépôt GitHub
3. Testez vos requêtes dans un client SQL comme DB Browser for SQLite

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Assurez-vous d'avoir créé la base de données** :
   ```bash
   cd exercice-02
   python creer_base_donnees.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Placez tous vos fichiers** dans ce dossier :
   - `solution.py`
   - `resultats.md`
   - Les fichiers CSV exportés

4. **Ajoutez et commitez vos fichiers** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 02 - Votre Nom"
   ```

5. **Poussez vers GitHub** :
   ```bash
   git push origin main
   ```
   
   Si vous avez forké le dépôt :
   ```bash
   git push origin votre-branche
   ```

6. **Créez une Pull Request** (si vous avez forké) ou vos fichiers seront directement visibles dans le dépôt principal.

### Structure de votre soumission

Votre dossier `solutions/votre-nom/` doit contenir :
- ✅ `solution.py` : Votre code Python complet avec toutes les requêtes
- ✅ `resultats.md` : Votre analyse et les requêtes SQL utilisées
- ✅ Les fichiers CSV exportés (si demandés)
- ✅ Un fichier `README.md` (optionnel) expliquant votre approche

### Vérification

Avant de pousser, vérifiez que :
- [ ] Toutes les requêtes fonctionnent correctement
- [ ] Le code est bien commenté
- [ ] Le fichier `resultats.md` est complet
- [ ] Les exports CSV sont présents

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom dans le chemin du dossier !


# Exercice 04 : Analyse de données avec Apache Spark

## 🎯 Objectifs

- Comprendre les concepts du Big Data
- Maîtriser Apache Spark pour le traitement distribué
- Implémenter des transformations sur de gros volumes de données
- Optimiser les performances Spark

## 📋 Prérequis

- Python 3.8+
- Bibliothèques : pyspark, pandas
- Java 8+ (requis pour Spark)
- Connaissances en programmation distribuée

## 📦 Installation

```bash
# Installer Java (si nécessaire)
# Windows: Télécharger depuis https://adoptium.net/
# Linux/Mac: sudo apt-get install openjdk-8-jdk

pip install pyspark pandas
```

## 🎓 Instructions

### Contexte

Vous travaillez avec un dataset de transactions e-commerce volumineux. Vous devez utiliser Spark pour analyser ces données de manière distribuée.

### Étape 1 : Configuration Spark

1. Créez un script `spark_config.py` qui configure Spark :
   - Mode local avec plusieurs cores
   - Configuration de la mémoire
   - Optimisation des paramètres

2. Créez une session Spark avec les bonnes configurations

### Étape 2 : Chargement des données

1. Chargez le dataset de transactions depuis un fichier CSV volumineux
2. Créez un DataFrame Spark
3. Explorez le schéma et les données
4. Affichez les statistiques de base

### Étape 3 : Transformations de base

1. **Filtrage** :
   - Filtrez les transactions supérieures à 100€
   - Filtrez par période (ex: dernière année)

2. **Sélection et projection** :
   - Sélectionnez les colonnes pertinentes
   - Créez de nouvelles colonnes calculées

3. **Agrégations** :
   - Calculez le CA total par client
   - Trouvez les produits les plus vendus
   - Calculez les statistiques par catégorie

### Étape 4 : Jointures et fenêtres

1. **Jointures** :
   - Joignez les transactions avec une table de référence produits
   - Joignez avec une table clients

2. **Fonctions de fenêtre (Window Functions)** :
   - Calculez le montant cumulé par client
   - Trouvez le top 3 des produits par catégorie
   - Calculez des moyennes mobiles

### Étape 5 : Optimisation

1. **Partitionnement** :
   - Repartitionnez les données de manière optimale
   - Utilisez le partitionnement par colonnes clés

2. **Caching** :
   - Identifiez les DataFrames à réutiliser
   - Utilisez le cache Spark efficacement

3. **Broadcast joins** :
   - Utilisez les broadcast joins pour les petites tables

### Étape 6 : Analyses avancées

1. **Analyse temporelle** :
   - Analysez les tendances par mois/trimestre
   - Détectez les saisonnalités

2. **Segmentation** :
   - Segmentez les clients (RFM analysis)
   - Identifiez les patterns de comportement

3. **Détection d'anomalies** :
   - Détectez les transactions suspectes
   - Identifiez les outliers

### Étape 7 : Export et visualisation

1. Exportez les résultats agrégés en CSV/Parquet
2. Créez des visualisations avec les données agrégées
3. Documentez vos analyses dans `resultats.md`

## 📁 Structure attendue

```
exercice-04/
├── README.md (ce fichier)
├── donnees/
│   └── transactions_large.csv (généré par le script)
├── solutions/
│   └── votre-nom/
│       ├── spark_config.py
│       ├── analysis.py
│       ├── generate_data.py (pour générer les données de test)
│       ├── resultats.md
│       └── outputs/
│           ├── ca_par_client.csv
│           └── produits_populaires.parquet
```

## ✅ Critères d'évaluation

- [ ] Configuration Spark optimale
- [ ] Transformations efficaces
- [ ] Utilisation appropriée des fonctions Spark
- [ ] Optimisations implémentées
- [ ] Analyses pertinentes
- [ ] Code bien documenté

## 💡 Conseils

- Utilisez `spark.sql()` pour les requêtes SQL complexes
- Évitez les collect() sur de gros datasets
- Utilisez les colonnes typées plutôt que les RDD
- Monitorer l'UI Spark (http://localhost:4040)
- Pensez à la persistance (cache, checkpoint)

## 🚀 Niveau avancé (Bonus)

- Implémentez un streaming avec Spark Streaming
- Utilisez MLlib pour des analyses prédictives
- Déployez sur un cluster (local ou cloud)
- Créez des UDF (User Defined Functions) optimisées

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Préparez votre environnement** :
   ```bash
   cd exercice-04
   ```
   
   2. **Générez les données nécessaires** (si applicable) :
   ```bash
   python generer_donnees.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Placez tous vos fichiers** dans ce dossier :
   - Votre code source
   - Votre fichier `resultats.md`
   - Tous les fichiers générés (graphiques, exports, etc.)

4. **Ajoutez et commitez vos fichiers** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 04 - Votre Nom"
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
- ✅ Tous vos fichiers de code source
- ✅ `resultats.md` : Votre analyse et résultats
- ✅ Tous les fichiers générés (graphiques, exports, etc.)
- ✅ Un fichier `README.md` (optionnel) expliquant votre approche

### Vérification

Avant de pousser, vérifiez que :
- [ ] Votre code fonctionne sans erreur
- [ ] Tous les fichiers sont présents
- [ ] La documentation est complète
- [ ] Les critères d'évaluation sont remplis

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom dans le chemin du dossier ! dans le README principal du dépôt pour soumettre votre solution.


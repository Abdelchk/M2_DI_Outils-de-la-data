# Exercice 04 : Apache Spark + Jupyter - Analyse Big Data

## 🎯 Objectifs

- Installer Apache Spark
- Utiliser Jupyter avec Spark
- Analyser de gros volumes de données
- Créer des visualisations interactives
- Maîtriser le traitement distribué

## 📋 Prérequis

- Python 3.8+
- Java 8+ (requis pour Spark)
- 4GB RAM minimum

## 📦 Installation

### Option 1 : Avec PySpark (Recommandé)

```bash
# Installer PySpark
pip install pyspark jupyter pandas matplotlib seaborn

# Vérifier l'installation
python -c "from pyspark.sql import SparkSession; print('OK')"
```

### Option 2 : Télécharger Spark

```bash
# Télécharger Spark depuis https://spark.apache.org/downloads.html
# Extraire et configurer
export SPARK_HOME=/chemin/vers/spark
export PATH=$PATH:$SPARK_HOME/bin
```

## 📊 Données

1. **Générez les données** :
   ```bash
   cd exercice-04
   python generer_donnees.py
   ```

## 🎓 Instructions

### Étape 1 : Démarrer Jupyter avec Spark

1. **Créez un notebook Jupyter** :
   ```bash
   jupyter notebook
   ```

2. **Dans le notebook, configurez Spark** :
   ```python
   from pyspark.sql import SparkSession
   
   spark = SparkSession.builder \
       .appName("AnalyseTransactions") \
       .master("local[4]") \
       .config("spark.sql.adaptive.enabled", "true") \
       .getOrCreate()
   
   spark
   ```

### Étape 2 : Charger les données

1. **Chargez le CSV** :
   ```python
   df = spark.read.csv(
       "donnees/transactions_large.csv",
       header=True,
       inferSchema=True
   )
   ```

2. **Explorez les données** :
   - Affichez le schéma
   - Comptez le nombre de lignes
   - Affichez quelques exemples

### Étape 3 : Transformations de base

1. **Filtrage** :
   - Transactions > 100€
   - Transactions d'une période spécifique

2. **Agrégations** :
   - CA total par client
   - Produits les plus vendus
   - Statistiques par catégorie

3. **Fonctions de fenêtre** :
   - Montant cumulé par client
   - Top 3 produits par catégorie

### Étape 4 : Analyses avancées

1. **Analyse temporelle** :
   - CA par mois
   - Tendances
   - Saisonnalités

2. **Segmentation** :
   - Clients par niveau de CA
   - Produits par performance

3. **Détection d'anomalies** :
   - Transactions suspectes
   - Outliers

### Étape 5 : Visualisations

1. **Utilisez Pandas pour visualiser** :
   ```python
   # Convertir en Pandas (pour petits résultats)
   df_pandas = resultat.toPandas()
   
   # Créer des graphiques
   import matplotlib.pyplot as plt
   import seaborn as sns
   ```

2. **Créez au moins 3 visualisations** :
   - Graphique de tendances
   - Graphique de comparaison
   - Graphique de répartition

### Étape 6 : Export des résultats

1. **Exportez en CSV** :
   ```python
   resultat.coalesce(1).write.csv(
       "output/resultats",
       header=True,
       mode="overwrite"
   )
   ```

2. **Exportez en Parquet** (recommandé) :
   ```python
   resultat.write.parquet(
       "output/resultats_parquet",
       mode="overwrite"
   )
   ```

## 📁 Structure attendue

```
exercice-04/
├── README.md (ce fichier)
├── donnees/
│   └── transactions_large.csv
├── notebooks/
│   └── analyse_spark.ipynb
└── solutions/
    └── votre-nom/
        ├── notebook.ipynb
        ├── output/ (résultats exportés)
        ├── resultats.md
        └── visualisations/ (graphiques)
```

## ✅ Critères d'évaluation

- [ ] Spark installé et fonctionnel
- [ ] Notebook Jupyter créé
- [ ] Données chargées et analysées
- [ ] Au moins 5 analyses effectuées
- [ ] Visualisations créées
- [ ] Résultats exportés
- [ ] Documentation complète

## 💡 Conseils

- Utilisez les DataFrames plutôt que les RDD
- Évitez les collect() sur gros datasets
- Utilisez le cache judicieusement
- Testez avec de petits échantillons d'abord
- Utilisez explain() pour voir le plan d'exécution

## 📚 Ressources

- Documentation Spark : https://spark.apache.org/docs/
- Guide PySpark : https://spark.apache.org/docs/latest/api/python/
- Tutoriels : https://spark.apache.org/docs/latest/quick-start.html

## 🆘 Aide

Si vous êtes bloqué :
1. Vérifiez que Java est installé
2. Consultez la documentation officielle
3. Ouvrez une issue sur le dépôt GitHub

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Générez les données** :
   ```bash
   cd exercice-04
   python generer_donnees.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Sauvegardez votre notebook Jupyter**
4. **Exportez vos résultats et visualisations**
5. **Créez un fichier `resultats.md`**

6. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 04 - Votre Nom"
   git push origin main
   ```

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !

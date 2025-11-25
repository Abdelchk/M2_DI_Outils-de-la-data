# Exercice 01 : Apache Superset - Business Intelligence Open Source

## 🎯 Objectifs

- Installer et configurer Apache Superset
- Créer des visualisations interactives
- Construire des dashboards professionnels
- Maîtriser un outil BI open source populaire

## 📋 Prérequis

- Python 3.8+
- Docker (recommandé) ou installation native
- Connaissances de base en SQL

## 📦 Installation

### Option 1 : Avec Docker (Recommandé - Plus simple)

```bash
# Télécharger et lancer Superset
docker run -d -p 8088:8088 --name superset apache/superset

# Initialiser la base de données
docker exec -it superset superset db upgrade

# Créer un utilisateur admin
docker exec -it superset superset fab create-admin \
  --username admin \
  --firstname Admin \
  --lastname User \
  --email admin@example.com \
  --password admin

# Initialiser Superset
docker exec -it superset superset init

# Accéder à Superset : http://localhost:8088
```

### Option 2 : Installation native

```bash
# Créer un environnement virtuel
python -m venv superset-env
source superset-env/bin/activate  # Linux/Mac
# ou superset-env\Scripts\activate  # Windows

# Installer Superset
pip install apache-superset

# Initialiser la base de données
superset db upgrade

# Créer un utilisateur admin
export FLASK_APP=superset
superset fab create-admin

# Initialiser Superset
superset init

# Démarrer Superset
superset run -p 8088 --with-threads --reload --debugger
```

## 📊 Données

1. **Générez les données** :
   ```bash
   cd exercice-01
   python generer_donnees.py
   ```

2. **Créez une base de données SQLite** avec les données :
   ```bash
   python creer_base_donnees.py
   ```

## 🎓 Instructions

### Étape 1 : Configuration initiale

1. **Accédez à Superset** : http://localhost:8088
2. **Connectez-vous** avec les identifiants créés (admin/admin par défaut)
3. **Explorez l'interface** :
   - Datasets : Sources de données
   - Charts : Visualisations
   - Dashboards : Tableaux de bord

### Étape 2 : Connexion à la base de données

1. **Allez dans Data > Databases**
2. **Cliquez sur "+ Database"**
3. **Configurez la connexion SQLite** :
   - Database Name : `Ventes E-commerce`
   - SQLAlchemy URI : `sqlite:///donnees/ventes.db`
   - Cliquez sur "Test Connection"
   - Sauvegardez

### Étape 3 : Créer un Dataset

1. **Allez dans Data > Datasets**
2. **Cliquez sur "+ Dataset"**
3. **Sélectionnez votre base de données** et la table `ventes`
4. **Nommez le dataset** : "Ventes"
5. **Explorez les colonnes** et leurs types

### Étape 4 : Créer des visualisations

Créez au moins 5 visualisations différentes :

1. **Graphique en barres** : Chiffre d'affaires par mois
   - Type : Bar Chart
   - X-axis : `date` (groupé par mois)
   - Y-axis : `montant_total` (SUM)

2. **Graphique en camembert** : Répartition par catégorie
   - Type : Pie Chart
   - Dimension : `categorie`
   - Metric : `montant_total` (SUM)

3. **Graphique de ligne** : Évolution des ventes dans le temps
   - Type : Line Chart
   - X-axis : `date`
   - Y-axis : `montant_total` (SUM)

4. **Table** : Top 10 produits
   - Type : Table View
   - Colonnes : `produit`, `quantite` (SUM), `montant_total` (SUM)
   - Trier par `montant_total` DESC
   - Limite : 10

5. **Graphique en barres empilées** : Ventes par catégorie et mois
   - Type : Stacked Bar Chart
   - X-axis : `date` (par mois)
   - Y-axis : `montant_total` (SUM)
   - Stack : `categorie`

### Étape 5 : Créer un Dashboard

1. **Allez dans Dashboards**
2. **Créez un nouveau dashboard** : "Analyse des Ventes"
3. **Ajoutez vos visualisations** :
   - Glissez-déposez vos charts
   - Organisez-les de manière logique
   - Ajustez les tailles

4. **Configurez les filtres** :
   - Ajoutez un filtre par date
   - Ajoutez un filtre par catégorie
   - Testez les filtres

### Étape 6 : Fonctionnalités avancées

1. **Créer des métriques personnalisées** :
   - Panier moyen
   - Taux de croissance
   - Pourcentages

2. **Utiliser SQL Lab** :
   - Créez des requêtes SQL complexes
   - Visualisez les résultats
   - Sauvegardez comme dataset

3. **Partager le dashboard** :
   - Exportez le dashboard en JSON
   - Documentez votre travail

## 📁 Structure attendue

```
exercice-01/
├── README.md (ce fichier)
├── donnees/
│   ├── ventes.csv
│   └── ventes.db (créé)
├── solutions/
│   └── votre-nom/
│       ├── dashboard_export.json
│       ├── screenshots/ (captures d'écran)
│       ├── resultats.md
│       └── requetes_sql.md (si applicable)
```

## ✅ Critères d'évaluation

- [ ] Superset installé et configuré
- [ ] Base de données connectée
- [ ] Au moins 5 visualisations créées
- [ ] Dashboard fonctionnel avec filtres
- [ ] Documentation complète avec captures d'écran
- [ ] Export du dashboard en JSON

## 💡 Conseils

- Utilisez SQL Lab pour des requêtes complexes
- Testez différents types de visualisations
- Organisez votre dashboard de manière logique
- Utilisez les couleurs de manière cohérente
- Documentez vos métriques personnalisées

## 📚 Ressources

- Documentation Superset : https://superset.apache.org/docs/
- Tutoriels : https://superset.apache.org/docs/intro
- Exemples de dashboards : https://github.com/apache/superset

## 🆘 Aide

Si vous êtes bloqué :
1. Consultez la documentation officielle
2. Regardez les tutoriels vidéo
3. Ouvrez une issue sur le dépôt GitHub

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Générez les données** :
   ```bash
   cd exercice-01
   python generer_donnees.py
   python creer_base_donnees.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Exportez votre dashboard** depuis Superset (JSON)
4. **Prenez des captures d'écran** de vos visualisations
5. **Créez un fichier `resultats.md`** avec vos analyses

6. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 01 - Votre Nom"
   git push origin main
   ```

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !

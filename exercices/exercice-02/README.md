# Exercice 02 : Metabase - Self-Service Business Intelligence

## 🎯 Objectifs

- Installer et configurer Metabase
- Créer des questions (queries) interactives
- Construire des dashboards sans code
- Maîtriser un outil BI self-service populaire

## 📋 Prérequis

- Java 11+ (pour Metabase)
- Docker (recommandé) ou installation native
- Connaissances de base en SQL (optionnel)

## 📦 Installation

### Option 1 : Avec Docker (Recommandé)

```bash
# Lancer Metabase
docker run -d -p 3000:3000 --name metabase metabase/metabase

# Accéder à Metabase : http://localhost:3000
# Configuration initiale au premier accès
```

### Option 2 : Installation native

```bash
# Télécharger le JAR depuis https://www.metabase.com/start/oss/
# Lancer Metabase
java -jar metabase.jar

# Accéder à http://localhost:3000
```

## 📊 Données

1. **Créez la base de données** :
   ```bash
   cd exercice-02
   python creer_base_donnees.py
   ```

## 🎓 Instructions

### Étape 1 : Configuration initiale

1. **Accédez à Metabase** : http://localhost:3000
2. **Première configuration** :
   - Créez un compte administrateur
   - Choisissez votre langue
   - Configurez les préférences

### Étape 2 : Ajouter une base de données

1. **Allez dans Settings > Admin > Databases**
2. **Cliquez sur "Add database"**
3. **Sélectionnez SQLite**
4. **Configurez la connexion** :
   - Nom : "Boutique E-commerce"
   - Fichier : Chemin vers `donnees/boutique.db`
   - Cliquez sur "Save"

### Étape 3 : Explorer les données

1. **Allez dans Browse Data**
2. **Explorez les tables** :
   - `clients`
   - `produits`
   - `commandes`
   - `details_commandes`
3. **Visualisez les données** de chaque table

### Étape 4 : Créer des Questions (Queries)

Créez au moins 6 questions différentes :

1. **Question simple** : Liste des clients
   - Table : `clients`
   - Affichez : nom, prénom, email, ville

2. **Question avec filtre** : Produits > 100€
   - Table : `produits`
   - Filtre : `prix > 100`
   - Trier par prix décroissant

3. **Question avec agrégation** : CA total
   - Table : `commandes`
   - Agrégation : SUM de `montant_total`

4. **Question avec jointure** : Commandes avec noms clients
   - Tables : `commandes` + `clients`
   - Jointure sur `client_id`
   - Affichez : commande_id, date, montant, nom client

5. **Question SQL personnalisée** : Top 5 clients par CA
   ```sql
   SELECT 
     c.nom, 
     c.prenom, 
     SUM(co.montant_total) as ca_total
   FROM clients c
   JOIN commandes co ON c.client_id = co.client_id
   GROUP BY c.client_id
   ORDER BY ca_total DESC
   LIMIT 5
   ```

6. **Question avec calcul** : Panier moyen par catégorie
   - Utilisez les jointures
   - Calculez le panier moyen

### Étape 5 : Créer des visualisations

Pour chaque question, créez une visualisation appropriée :

1. **Table** : Pour les listes
2. **Bar Chart** : Pour les comparaisons
3. **Line Chart** : Pour les tendances temporelles
4. **Pie Chart** : Pour les répartitions
5. **Number** : Pour les métriques uniques

### Étape 6 : Créer un Dashboard

1. **Créez un nouveau dashboard** : "Analyse Boutique"
2. **Ajoutez vos questions** :
   - Glissez-déposez vos questions
   - Organisez-les par thème
   - Ajustez les tailles

3. **Ajoutez des filtres** :
   - Filtre par date
   - Filtre par catégorie de produit
   - Filtre par client

4. **Configurez les paramètres** :
   - Auto-refresh
   - Liens entre questions
   - Actions personnalisées

### Étape 7 : Fonctionnalités avancées

1. **Créer des modèles de données** :
   - Définir les relations entre tables
   - Créer des métriques réutilisables

2. **Utiliser les alertes** :
   - Créer une alerte si CA < seuil
   - Configurer les notifications

3. **Partager le dashboard** :
   - Créer un lien public (optionnel)
   - Exporter les données

## 📁 Structure attendue

```
exercice-02/
├── README.md (ce fichier)
├── donnees/
│   └── boutique.db
├── solutions/
│   └── votre-nom/
│       ├── screenshots/ (captures d'écran)
│       ├── questions_export.json (si possible)
│       ├── resultats.md
│       └── requetes_sql.md
```

## ✅ Critères d'évaluation

- [ ] Metabase installé et configuré
- [ ] Base de données connectée
- [ ] Au moins 6 questions créées
- [ ] Visualisations appropriées pour chaque question
- [ ] Dashboard fonctionnel avec filtres
- [ ] Documentation complète

## 💡 Conseils

- Utilisez l'éditeur visuel pour commencer
- Passez à SQL pour les requêtes complexes
- Testez vos questions avant de les ajouter au dashboard
- Organisez vos dashboards par thème métier
- Utilisez les modèles de données pour simplifier

## 📚 Ressources

- Documentation Metabase : https://www.metabase.com/docs/
- Guide de démarrage : https://www.metabase.com/learn/getting-started
- Exemples de questions : https://www.metabase.com/learn

## 🆘 Aide

Si vous êtes bloqué :
1. Consultez la documentation officielle
2. Utilisez le mode "Simple question" pour commencer
3. Ouvrez une issue sur le dépôt GitHub

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Créez la base de données** :
   ```bash
   cd exercice-02
   python creer_base_donnees.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Prenez des captures d'écran** :
   - Vos questions
   - Votre dashboard
   - Les visualisations

4. **Créez un fichier `resultats.md`** avec :
   - Description de vos questions
   - Analyses effectuées
   - Insights découverts

5. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 02 - Votre Nom"
   git push origin main
   ```

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !

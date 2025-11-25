# Atelier 01 : Projet complet - Dashboard analytique

## 🎯 Objectifs

- Mettre en pratique tous les concepts appris
- Créer un projet complet de bout en bout
- Développer un dashboard interactif
- Présenter et documenter un projet data

## 📋 Prérequis

- Tous les exercices précédents complétés
- Bibliothèques : pandas, matplotlib, seaborn, plotly, streamlit (ou dash)
- Connaissances en visualisation de données

## 📦 Installation

```bash
pip install pandas matplotlib seaborn plotly streamlit
```

## 🎓 Instructions

### Contexte du projet

Vous êtes data analyst dans une entreprise e-commerce. Votre mission est de créer un dashboard analytique complet pour aider la direction à prendre des décisions stratégiques.

### Phase 1 : Préparation des données (2h)

1. **Collecte et nettoyage** :
   - Utilisez les données des exercices précédents ou créez un dataset réaliste
   - Nettoyez et préparez les données
   - Créez un pipeline de préparation reproductible

2. **Enrichissement** :
   - Ajoutez des métriques calculées
   - Créez des segments de clients
   - Calculez des KPIs métier

### Phase 2 : Analyses exploratoires (3h)

1. **Analyses descriptives** :
   - Statistiques générales
   - Distributions des variables
   - Corrélations

2. **Analyses métier** :
   - Analyse des ventes (évolution, tendances)
   - Analyse des clients (segmentation, comportement)
   - Analyse des produits (performance, catégories)
   - Analyse de la rentabilité

3. **Insights** :
   - Identifiez les opportunités
   - Détectez les problèmes
   - Proposez des recommandations

### Phase 3 : Visualisations (3h)

Créez au moins 10 visualisations interactives :

1. **Tableaux de bord** :
   - Vue d'ensemble avec KPIs principaux
   - Vue temporelle (évolution dans le temps)
   - Vue géographique (si applicable)
   - Vue produits/catégories

2. **Graphiques** :
   - Graphiques de tendances (lignes)
   - Comparaisons (barres, colonnes)
   - Répartitions (camemberts, treemaps)
   - Corrélations (heatmaps, scatter)
   - Distributions (histogrammes, boxplots)

3. **Interactivité** :
   - Filtres par période, catégorie, etc.
   - Drill-down (navigation hiérarchique)
   - Tooltips informatifs

### Phase 4 : Dashboard interactif (4h)

1. **Choix de l'outil** :
   - Streamlit (recommandé pour débutants)
   - Dash (plus avancé)
   - Ou solution custom avec Flask/FastAPI

2. **Structure du dashboard** :
   - Page d'accueil avec vue d'ensemble
   - Pages dédiées par thème (ventes, clients, produits)
   - Page d'analyse approfondie

3. **Fonctionnalités** :
   - Filtres interactifs
   - Mise à jour dynamique des graphiques
   - Export des données
   - Responsive design

### Phase 5 : Documentation et présentation (2h)

1. **Documentation technique** :
   - README complet
   - Documentation du code
   - Guide d'installation et d'utilisation

2. **Présentation métier** :
   - Slides de présentation (5-10 slides)
   - Storytelling des données
   - Recommandations actionnables

3. **Rapport d'analyse** :
   - Méthodologie
   - Résultats clés
   - Insights et recommandations

## 📁 Structure attendue

```
atelier-01/
├── README.md (ce fichier)
├── donnees/
│   ├── raw/ (données brutes)
│   ├── processed/ (données nettoyées)
│   └── final/ (données finales)
├── notebooks/
│   └── exploration.ipynb
├── src/
│   ├── data_preparation.py
│   ├── analysis.py
│   └── visualizations.py
├── dashboard/
│   ├── app.py (application principale)
│   ├── pages/
│   │   ├── overview.py
│   │   ├── sales.py
│   │   └── customers.py
│   └── components/
│       └── charts.py
├── presentation/
│   ├── slides.pdf
│   └── rapport_analyse.md
└── solutions/
    └── votre-nom/
        └── (votre solution complète)
```

## ✅ Critères d'évaluation

- [ ] Projet complet et fonctionnel
- [ ] Code propre et bien organisé
- [ ] Dashboard interactif et esthétique
- [ ] Analyses pertinentes et approfondies
- [ ] Visualisations claires et informatives
- [ ] Documentation complète
- [ ] Présentation professionnelle

## 💡 Conseils

- Commencez simple, itérez ensuite
- Testez votre dashboard avec des utilisateurs
- Pensez à l'expérience utilisateur
- Utilisez des couleurs cohérentes
- Ajoutez des annotations aux graphiques
- Racontez une histoire avec vos données

## 🚀 Fonctionnalités avancées (Bonus)

- Prédictions avec machine learning
- Alertes automatiques sur anomalies
- Export PDF automatique des rapports
- Authentification utilisateur
- Base de données en temps réel
- Déploiement en production (Heroku, AWS, etc.)

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre atelier sur GitHub

1. **Créez votre dossier de solution** :
   ```bash
   cd atelier-01
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

2. **Placez tous vos fichiers** dans ce dossier :
   - Tous vos fichiers de code
   - Votre documentation
   - Tous les fichiers générés

3. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Atelier 01 - Votre Nom"
   git push origin main
   ```

4. **Créez une Pull Request** si vous avez forké le dépôt.

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom ! dans le README principal du dépôt pour soumettre votre solution.




# Atelier 02 : Machine Learning Pipeline

## 🎯 Objectifs

- Construire un pipeline ML complet
- Préparer les données pour le ML
- Entraîner et évaluer des modèles
- Déployer un modèle en production

## 📋 Prérequis

- Python 3.8+
- Bibliothèques : pandas, scikit-learn, xgboost, matplotlib, joblib
- Connaissances en machine learning

## 📦 Installation

```bash
pip install pandas scikit-learn xgboost matplotlib seaborn joblib
```

## 🎓 Instructions

### Contexte

Vous devez créer un système de prédiction pour un problème métier (ex: prédiction de churn, prévision de ventes, classification de produits, etc.).

### Phase 1 : Définition du problème (1h)

1. **Choix du problème** :
   - Sélectionnez un problème métier concret
   - Définissez la variable cible
   - Identifiez les métriques de succès

2. **Collecte de données** :
   - Utilisez un dataset public (Kaggle, UCI, etc.)
   - Ou créez un dataset synthétique réaliste
   - Documentez la source des données

### Phase 2 : Exploration et préparation (3h)

1. **EDA approfondie** :
   - Analyse univariée et multivariée
   - Détection des outliers
   - Analyse des corrélations
   - Visualisations exploratoires

2. **Feature Engineering** :
   - Création de nouvelles features
   - Encodage des variables catégorielles
   - Normalisation/standardisation
   - Gestion des valeurs manquantes

3. **Sélection de features** :
   - Analyse de l'importance des features
   - Sélection des features pertinentes
   - Réduction de dimensionnalité (si nécessaire)

### Phase 3 : Modélisation (4h)

1. **Baseline** :
   - Implémentez un modèle simple (régression linéaire, arbre de décision)
   - Établissez une baseline de performance

2. **Modèles multiples** :
   - Testez au moins 3 algorithmes différents :
     * Modèle linéaire (Logistic Regression, Linear Regression)
     * Modèle d'ensemble (Random Forest, XGBoost)
     * Modèle avancé (SVM, Neural Network si temps)

3. **Optimisation** :
   - Hyperparameter tuning (GridSearch/RandomSearch)
   - Validation croisée
   - Optimisation des métriques

### Phase 4 : Évaluation et sélection (2h)

1. **Évaluation rigoureuse** :
   - Métriques appropriées (accuracy, precision, recall, F1, ROC-AUC, etc.)
   - Validation sur ensemble de test
   - Analyse des erreurs

2. **Interprétabilité** :
   - Feature importance
   - SHAP values (si possible)
   - Visualisation des décisions du modèle

3. **Sélection du meilleur modèle** :
   - Comparaison des modèles
   - Justification du choix
   - Analyse des trade-offs

### Phase 5 : Pipeline de production (3h)

1. **Création du pipeline** :
   - Pipeline de preprocessing
   - Pipeline d'entraînement
   - Pipeline de prédiction
   - Utilisez sklearn.pipeline

2. **Sauvegarde et chargement** :
   - Sauvegardez le modèle entraîné (joblib/pickle)
   - Créez une fonction de chargement
   - Versioning du modèle

3. **API de prédiction** :
   - Créez une API REST (Flask/FastAPI)
   - Endpoint de prédiction
   - Validation des inputs
   - Gestion d'erreurs

4. **Tests** :
   - Tests unitaires du pipeline
   - Tests d'intégration de l'API
   - Tests de performance

### Phase 6 : Documentation et déploiement (2h)

1. **Documentation** :
   - Documentation du modèle (méthodologie, performances)
   - Guide d'utilisation de l'API
   - README complet

2. **Déploiement** (optionnel) :
   - Containerisation (Docker)
   - Déploiement local ou cloud
   - Monitoring basique

## 📁 Structure attendue

```
atelier-02/
├── README.md (ce fichier)
├── donnees/
│   ├── raw/ (données brutes)
│   └── processed/ (données préparées)
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── models/
│   │   ├── train.py
│   │   └── predict.py
│   └── api/
│       └── app.py
├── models/
│   └── (modèles sauvegardés)
├── tests/
│   └── test_pipeline.py
└── solutions/
    └── votre-nom/
        └── (votre solution complète)
```

## ✅ Critères d'évaluation

- [ ] Pipeline ML complet et fonctionnel
- [ ] Feature engineering pertinent
- [ ] Modèles bien entraînés et évalués
- [ ] Code propre et modulaire
- [ ] API fonctionnelle
- [ ] Documentation complète
- [ ] Performance du modèle justifiée

## 💡 Conseils

- Commencez simple, complexifiez progressivement
- Documentez chaque étape
- Visualisez vos résultats
- Testez sur différents datasets
- Pensez à la production dès le début
- Validez avec des métriques métier

## 🚀 Fonctionnalités avancées (Bonus)

- AutoML (Auto-sklearn, TPOT)
- Deep Learning (TensorFlow/PyTorch)
- A/B testing du modèle
- Monitoring en production (MLflow)
- Retraining automatique
- Explicabilité avancée (LIME, SHAP)

## 📤 Soumission

Suivez les instructions dans le README principal du dépôt pour soumettre votre solution.

**Durée estimée totale : 15-17 heures**


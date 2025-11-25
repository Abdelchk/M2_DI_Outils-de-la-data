# Exercice 03 : Pipeline ETL avec Python

## 🎯 Objectifs

- Comprendre le concept de pipeline ETL (Extract, Transform, Load)
- Implémenter un pipeline complet de traitement de données
- Gérer les erreurs et la validation des données
- Optimiser les performances du pipeline

## 📋 Prérequis

- Python 3.8+
- Bibliothèques : pandas, requests, sqlalchemy
- Connaissances en programmation orientée objet

## 📦 Installation

```bash
pip install pandas requests sqlalchemy
```

## 🎓 Instructions

### Contexte

Vous devez créer un pipeline ETL qui :
1. **Extract** : Récupère des données depuis plusieurs sources (API, fichiers CSV, base de données)
2. **Transform** : Nettoie, transforme et enrichit les données
3. **Load** : Charge les données transformées dans une destination finale

### Étape 1 : Architecture du pipeline

1. Créez une structure de classes pour votre pipeline :
   - `Extractor` : Classe abstraite pour l'extraction
   - `Transformer` : Classe pour les transformations
   - `Loader` : Classe abstraite pour le chargement
   - `ETLPipeline` : Classe principale qui orchestre le tout

2. Implémentez le pattern Strategy pour permettre différents types d'extracteurs et loaders

### Étape 2 : Extraction (Extract)

Créez plusieurs extracteurs :

1. **CSVExtractor** : Lit des données depuis un fichier CSV
2. **APIExtractor** : Récupère des données depuis une API REST
3. **DatabaseExtractor** : Extrait des données depuis une base de données SQLite

### Étape 3 : Transformation (Transform)

Implémentez les transformations suivantes :

1. **Nettoyage** :
   - Suppression des doublons
   - Gestion des valeurs manquantes
   - Normalisation des formats (dates, nombres, textes)

2. **Enrichissement** :
   - Ajout de colonnes calculées
   - Jointures avec des données de référence
   - Calculs statistiques

3. **Validation** :
   - Vérification des types de données
   - Validation des contraintes métier
   - Détection d'anomalies

4. **Agrégation** :
   - Regroupements par catégories
   - Calculs de métriques agrégées

### Étape 4 : Chargement (Load)

Créez plusieurs loaders :

1. **CSVLoader** : Sauvegarde dans un fichier CSV
2. **DatabaseLoader** : Charge dans une base de données SQLite
3. **JSONLoader** : Exporte en format JSON

### Étape 5 : Orchestration

1. Créez la classe `ETLPipeline` qui :
   - Configure les extracteurs, transformers et loaders
   - Exécute le pipeline étape par étape
   - Gère les erreurs et les logs
   - Fournit des métriques d'exécution

2. Implémentez un système de logging pour tracer l'exécution

3. Ajoutez la gestion des erreurs avec retry logic

### Étape 6 : Tests et validation

1. Créez des tests unitaires pour chaque composant
2. Testez le pipeline complet avec des données réelles
3. Mesurez les performances (temps d'exécution, mémoire)
4. Documentez les résultats

## 📁 Structure attendue

```
exercice-03/
├── README.md (ce fichier)
├── donnees/
│   ├── source1.csv
│   ├── source2.csv
│   └── reference_data.json
├── solutions/
│   └── votre-nom/
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── extractors.py
│       │   ├── transformers.py
│       │   ├── loaders.py
│       │   └── pipeline.py
│       ├── tests/
│       │   └── test_pipeline.py
│       ├── main.py
│       ├── config.py
│       ├── resultats.md
│       └── logs/
```

## ✅ Critères d'évaluation

- [ ] Architecture propre et modulaire
- [ ] Code respectant les principes SOLID
- [ ] Gestion d'erreurs robuste
- [ ] Logging complet
- [ ] Tests unitaires présents
- [ ] Documentation claire
- [ ] Pipeline fonctionnel end-to-end

## 💡 Conseils

- Utilisez des classes abstraites (ABC) pour définir les interfaces
- Implémentez le pattern Strategy pour la flexibilité
- Utilisez le module `logging` pour les logs
- Pensez à la performance : utilisez des générateurs pour les gros volumes
- Documentez chaque classe et méthode

## 🚀 Niveau avancé (Bonus)

- Ajoutez un système de parallélisation (multiprocessing)
- Implémentez un système de cache pour éviter les re-extractions
- Créez un dashboard de monitoring du pipeline
- Ajoutez la validation de schéma avec Pydantic

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Préparez votre environnement** :
   ```bash
   cd exercice-03
   ```
   
   2. **Installez les dépendances** :
   ```bash
   # Installez les outils requis selon les instructions du README
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
   git commit -m "Solution exercice 03 - Votre Nom"
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


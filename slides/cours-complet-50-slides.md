# OUTILS DE LA DATA
## Master 2 - Développement Informatique

**Formateur : Abid Hamza**

---

# SLIDE 1 : BIENVENUE

Bienvenue dans cette formation sur les Outils de la Data !

Je suis Abid Hamza, votre formateur.

Cette formation vous permettra de maîtriser les outils essentiels pour travailler avec les données.

---

# SLIDE 2 : PRÉSENTATION DU COURS

**Objectifs de cette formation :**

- Comprendre l'écosystème des outils de données
- Maîtriser les outils open source professionnels
- Créer des dashboards et visualisations
- Construire des pipelines de données
- Choisir les bons outils selon le contexte

---

# SLIDE 3 : PLAN DU COURS

1. Introduction aux outils de la data
2. Écosystème des outils de données
3. Outils de collecte et ingestion
4. Outils de stockage
5. Outils de traitement et transformation
6. Outils d'analyse et visualisation
7. Outils de machine learning
8. Outils de déploiement et orchestration
9. Choix des outils selon le contexte
10. Bonnes pratiques et recommandations

---

# SLIDE 4 : POURQUOI LES OUTILS DE DATA ?

**Le monde génère des données massives :**

- Chaque jour, des milliards de données sont créées
- Les entreprises ont besoin d'exploiter ces données
- Les outils manuels ne suffisent plus
- Il faut des outils spécialisés et performants

**Exemple :** Une application mobile peut générer des millions d'événements par jour.

---

# SLIDE 5 : LES 4 V DU BIG DATA

**Volume :** Quantité massive de données
- Exemple : Des téraoctets ou pétaoctets de données

**Variété :** Différents formats de données
- Structurées : Tables SQL
- Semi-structurées : JSON, XML
- Non structurées : Textes, images, vidéos

**Vélocité :** Vitesse de génération et traitement
- Données en temps réel
- Traitement continu

**Valeur :** Extraction d'insights utiles
- Prédictions
- Recommandations
- Décisions stratégiques

---

# SLIDE 6 : LE DÉFI DES DONNÉES

```
┌─────────────────────────────────────┐
│     DONNÉES BRUTES (Sources)        │
│  - APIs, fichiers, bases de données │
│  - Formats variés, volumes importants│
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│        COLLECTE ET INGESTION       │
│  - Extraire les données             │
│  - Les charger dans un système      │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│            STOCKAGE                 │
│  - Data Warehouse                   │
│  - Data Lake                        │
│  - Bases de données                │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│        TRAITEMENT                   │
│  - Nettoyer                         │
│  - Transformer                      │
│  - Enrichir                         │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│        ANALYSE ET INSIGHTS          │
│  - Statistiques                     │
│  - Visualisations                   │
│  - Décisions                        │
└─────────────────────────────────────┘
```

---

# SLIDE 7 : OBJECTIFS DE CE COURS

À la fin de cette formation, vous serez capable de :

1. **Identifier** les outils adaptés à chaque situation
2. **Installer** et configurer des outils open source
3. **Utiliser** les outils pour analyser des données
4. **Créer** des dashboards et visualisations
5. **Construire** des pipelines de données complets
6. **Choisir** les bons outils selon le contexte

---

# SLIDE 8 : ARCHITECTURE D'UN PIPELINE DE DONNÉES

```
┌──────────────────────────────────────────────┐
│           SOURCES DE DONNÉES                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │   APIs   │  │  Fichiers │  │   Bases  │  │
│  │          │  │  (CSV...) │  │  données │  │
│  └──────────┘  └──────────┘  └──────────┘  │
└──────────────┬───────────────────────────────┘
               │
               ↓
┌──────────────────────────────────────────────┐
│         INGESTION (ETL/ELT)                  │
│  - Extraction des données                    │
│  - Transformation                            │
│  - Chargement                                │
└──────────────┬───────────────────────────────┘
               │
               ↓
┌──────────────────────────────────────────────┐
│            STOCKAGE                          │
│  ┌──────────────┐      ┌──────────────┐      │
│  │ Data        │      │ Data         │      │
│  │ Warehouse   │      │ Lake         │      │
│  └──────────────┘      └──────────────┘      │
└──────────────┬───────────────────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌──────────────┐
│  TRAITEMENT  │  │   ANALYSE    │
│  (Spark)     │  │  (BI Tools) │
└──────┬───────┘  └──────┬───────┘
       │                 │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │ VISUALISATION   │
       │  (Dashboards)   │
       └─────────────────┘
```

---

# SLIDE 9 : CATÉGORIES D'OUTILS

**1. Collecte et Ingestion**
- Extraction depuis APIs
- Web scraping
- ETL/ELT pipelines

**2. Stockage**
- Bases de données relationnelles
- Data Warehouses
- Data Lakes
- Bases NoSQL

**3. Traitement**
- Batch processing
- Stream processing
- Transformation

**4. Analyse**
- Business Intelligence
- Analytics
- Reporting

**5. Machine Learning**
- Frameworks ML
- MLOps
- AutoML

**6. Orchestration**
- Workflow management
- Scheduling
- Monitoring

---

# SLIDE 10 : OUTILS DE COLLECTE - APIS

**Extraction depuis APIs REST :**

```
Application → API REST → Données JSON/XML
                ↓
         Transformation
                ↓
         Stockage
```

**Outils Python :**
- `requests` : Bibliothèque simple pour requêtes HTTP
- `pandas` : Manipulation de données
- `json` : Parsing JSON

**Exemple d'utilisation :**
```python
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
```

---

# SLIDE 11 : OUTILS DE COLLECTE - WEB SCRAPING

**Web Scraping :** Extraire des données depuis des sites web

```
Site Web → Scraper → Données structurées
```

**Outils :**
- **BeautifulSoup** : Parsing HTML simple
- **Scrapy** : Framework complet pour scraping à grande échelle
- **Selenium** : Automatisation de navigateur

**Cas d'usage :**
- Collecte de prix
- Extraction d'articles
- Monitoring de sites

---

# SLIDE 12 : OUTILS ETL/ELT

**ETL : Extract, Transform, Load**
**ELT : Extract, Load, Transform**

**Apache Airflow :**
- Orchestration de workflows
- Interface web
- Gestion des dépendances
- Open source

**Talend :**
- Plateforme ETL complète
- Interface graphique
- Connecteurs multiples

**Apache NiFi :**
- Ingestion en temps réel
- Interface de flux visuelle

---

# SLIDE 13 : SCHÉMA D'INGESTION

```
┌─────────────────────────────────────┐
│      SOURCES MULTIPLES              │
│                                     │
│  ┌──────┐  ┌──────┐  ┌──────┐      │
│  │ APIs │  │Files │  │  DBs │      │
│  └──┬───┘  └──┬───┘  └──┬───┘      │
│     │         │         │          │
│     └─────┬───┴─────┬───┘          │
│           │         │              │
└───────────┼─────────┼──────────────┘
            │         │
            ↓         ↓
    ┌───────────────┐
    │  ETL/ELT      │
    │  Pipeline     │
    └───────┬───────┘
            │
            ↓
    ┌───────────────┐
    │ Data Warehouse│
    │   / Data Lake │
    └───────────────┘
```

---

# SLIDE 14 : BASES DE DONNÉES RELATIONNELLES

**PostgreSQL :**
- Open source et robuste
- Support JSON, arrays
- Extensions puissantes
- Excellent pour applications complexes

**MySQL / MariaDB :**
- Très populaire
- Performant pour lectures
- Facile à administrer
- Standard du web

**SQL Server :**
- Solution Microsoft
- BI intégré
- Support entreprise

---

# SLIDE 15 : DATA WAREHOUSES

**Snowflake :**
- Cloud-native
- Séparation stockage/compute
- Scaling automatique
- Pay-as-you-go

**BigQuery (Google) :**
- Serverless
- Analytics intégré
- ML intégré
- Pas de maintenance

**Redshift (AWS) :**
- Data warehouse cloud AWS
- Performances élevées
- Intégration AWS native

---

# SLIDE 16 : DATA LAKES

**Apache Hadoop HDFS :**
- Stockage distribué
- Écosystème Hadoop
- Open source
- Scalable horizontalement

**AWS S3 :**
- Stockage objet
- Scalabilité infinie
- Durabilité 99.999999999%
- Coût très faible

**Azure Data Lake :**
- Solution Microsoft
- Analytics intégré
- Sécurité avancée

---

# SLIDE 17 : BASES NOSQL

**MongoDB :**
- Orienté documents (JSON-like)
- Schéma flexible
- Excellent pour données non structurées
- Scaling horizontal

**Cassandra :**
- Wide-column store
- Haute disponibilité
- Pas de point de défaillance
- Idéal pour time-series

**Redis :**
- In-memory database
- Très rapide
- Cache et sessions
- Structures de données avancées

---

# SLIDE 18 : GUIDE DE CHOIX DE STOCKAGE

```
┌─────────────────────────────────────┐
│   Type de données structurées ?     │
│   → OUI → SQL (PostgreSQL, MySQL)   │
└─────────────────────────────────────┘
           │
           ↓ NON
┌─────────────────────────────────────┐
│   Données semi-structurées ?        │
│   → OUI → NoSQL (MongoDB)          │
└─────────────────────────────────────┘
           │
           ↓ NON
┌─────────────────────────────────────┐
│   Besoin d'analytics ?              │
│   → OUI → Data Warehouse           │
└─────────────────────────────────────┘
           │
           ↓ NON
┌─────────────────────────────────────┐
│   Big Data ?                        │
│   → OUI → Data Lake (S3, HDFS)      │
└─────────────────────────────────────┘
```

---

# SLIDE 19 : TRAITEMENT BATCH - APACHE SPARK

**Apache Spark :**
- Traitement distribué à grande échelle
- Support Python, Scala, Java, R
- MLlib pour machine learning
- Streaming intégré
- Très performant

**Architecture :**
```
Driver → Cluster Manager → Workers
           ↓
    Traitement distribué
    sur plusieurs machines
```

**Avantages :**
- Traite des téraoctets de données
- Tolérance aux pannes
- In-memory processing

---

# SLIDE 20 : TRAITEMENT BATCH - PANDAS

**Pandas :**
- Bibliothèque Python standard
- Manipulation de données intuitive
- Nombreuses fonctions intégrées
- Excellent pour données < 10GB

**Opérations principales :**
- Lecture/écriture de fichiers
- Filtrage et sélection
- Agrégations
- Jointures
- Transformations

**Limitation :** Mémoire RAM (données doivent tenir en mémoire)

---

# SLIDE 21 : TRAITEMENT STREAMING - KAFKA

**Apache Kafka :**
- Message broker distribué
- Haute performance (millions msg/sec)
- Durabilité des messages
- Scalable horizontalement

**Architecture :**
```
Producers → Kafka Cluster → Consumers
              ↓
        Topics (partitions)
```

**Cas d'usage :**
- Event streaming
- Log aggregation
- Real-time analytics

---

# SLIDE 22 : TRAITEMENT STREAMING - FLINK

**Apache Flink :**
- Stream processing avancé
- Event time processing
- Faible latence
- State management

**Caractéristiques :**
- Traitement en temps réel
- Gestion d'état
- Exactly-once semantics
- Windowing avancé

**Exemple :** Analyse de transactions en temps réel

---

# SLIDE 23 : OUTILS DE TRANSFORMATION - DBT

**dbt (data build tool) :**
- Transformation SQL uniquement
- Versioning avec Git
- Testing intégré
- Documentation automatique
- Workflow moderne

**Principe :**
```
Sources → Staging → Intermediate → Marts
```

**Avantages :**
- Code SQL réutilisable
- Tests automatiques
- Documentation générée
- Collaboration facilitée

---

# SLIDE 24 : SCHÉMA DE TRAITEMENT

```
┌─────────────────────────────────────┐
│        DONNÉES BRUTES               │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌──────────────┐
│    BATCH     │  │   STREAMING  │
│              │  │              │
│  - Spark     │  │  - Kafka     │
│  - Pandas    │  │  - Flink     │
│  - Dask      │  │  - Storm     │
│              │  │              │
│  Périodique  │  │  Temps réel  │
└──────┬───────┘  └──────┬───────┘
       │                 │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │ DONNÉES         │
       │ TRANSFORMÉES   │
       └─────────────────┘
```

---

# SLIDE 25 : BUSINESS INTELLIGENCE - TABLEAU

**Tableau :**
- Visualisations avancées
- Dashboards interactifs
- Connecteurs multiples
- Self-service BI
- Leader du marché

**Points forts :**
- Interface intuitive
- Visualisations puissantes
- Partage facile
- Mobile support

**Prix :** Commercial (payant)

---

# SLIDE 26 : BUSINESS INTELLIGENCE - POWER BI

**Power BI (Microsoft) :**
- Intégration Office 365
- Self-service BI
- Cloud et on-premise
- Prix compétitif

**Points forts :**
- Intégration Microsoft
- Facile à apprendre
- Version gratuite disponible
- Large communauté

---

# SLIDE 27 : BI OPEN SOURCE - APACHE SUPERSET

**Apache Superset :**
- Open source et gratuit
- Dashboards interactifs
- Support SQL natif
- Nombreux types de visualisations
- Développé par Airbnb

**Installation :**
```bash
docker run -d -p 8088:8088 apache/superset
```

**Avantages :**
- Gratuit
- Puissant
- Communauté active
- Extensible

---

# SLIDE 28 : BI OPEN SOURCE - METABASE

**Metabase :**
- Simple à utiliser
- Self-service pour non-techniques
- Open source
- Installation facile

**Points forts :**
- Interface intuitive
- Questions sans code
- Partage facile
- Version cloud disponible

**Installation :**
```bash
docker run -d -p 3000:3000 metabase/metabase
```

---

# SLIDE 29 : MONITORING - GRAFANA

**Grafana :**
- Monitoring et observabilité
- Excellent pour time-series
- Alerting intégré
- Nombreux plugins
- Standard pour le monitoring

**Cas d'usage :**
- Monitoring d'applications
- Métriques système
- Dashboards opérationnels
- Alertes automatiques

---

# SLIDE 30 : VISUALISATION PYTHON - MATPLOTLIB

**Matplotlib :**
- Bibliothèque de base Python
- Très flexible
- Standard de facto
- Contrôle total

**Types de graphiques :**
- Lignes, barres, camemberts
- Scatter plots
- Histogrammes
- 3D

**Utilisation :**
```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
```

---

# SLIDE 31 : VISUALISATION PYTHON - PLOTLY

**Plotly :**
- Visualisations interactives
- Dashboards web
- Support 3D et animations
- Export facile

**Avantages :**
- Interactivité
- Beaux graphiques
- Dashboards web
- Version open source

---

# SLIDE 32 : SCHÉMA D'ANALYSE

```
┌─────────────────────────────────────┐
│   DONNÉES PRÉPARÉES                  │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌──────────────┐
│ EXPLORATION  │  │ VISUALISATION│
│              │  │              │
│ - Jupyter    │  │ - Matplotlib │
│ - Pandas     │  │ - Plotly     │
│ - Stats      │  │ - Seaborn    │
└──────┬───────┘  └──────┬───────┘
       │                 │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │   DASHBOARDS    │
       │                 │
       │ - Superset      │
       │ - Metabase      │
       │ - Grafana       │
       └─────────────────┘
```

---

# SLIDE 33 : MACHINE LEARNING - SCIKIT-LEARN

**Scikit-learn :**
- Machine learning Python
- Algorithmes classiques complets
- Interface uniforme
- Facile à utiliser
- Documentation excellente

**Algorithmes :**
- Classification
- Régression
- Clustering
- Réduction de dimensionnalité

---

# SLIDE 34 : MACHINE LEARNING - TENSORFLOW

**TensorFlow (Google) :**
- Deep learning avancé
- Production-ready
- TensorBoard pour visualisation
- Support mobile
- Large communauté

**Cas d'usage :**
- Réseaux de neurones
- Computer vision
- NLP
- Recommandations

---

# SLIDE 35 : MACHINE LEARNING - PYTORCH

**PyTorch (Facebook/Meta) :**
- Deep learning
- Research-friendly
- Graph computation dynamique
- Interface Python native
- Très populaire en recherche

**Avantages :**
- Flexible
- Debugging facile
- Adoption croissante

---

# SLIDE 36 : MLOPS - MLFLOW

**MLflow :**
- Gestion d'expériences ML
- Tracking des métriques
- Versioning des modèles
- Déploiement simplifié
- Open source

**Fonctionnalités :**
- Suivi des expériences
- Comparaison de modèles
- Reproducibilité
- Déploiement

---

# SLIDE 37 : PIPELINE ML TYPIQUE

```
┌─────────────────────────────────────┐
│     DONNÉES BRUTES                   │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   ETL/ELT (Extraction, Transformation)│
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   FEATURE ENGINEERING               │
│   - Sélection de features           │
│   - Création de nouvelles features  │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   MODÉLISATION                      │
│   - Scikit-learn                    │
│   - TensorFlow / PyTorch            │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   ÉVALUATION                        │
│   - Métriques                       │
│   - Validation croisée              │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   DÉPLOIEMENT                       │
│   - MLflow                          │
│   - Kubeflow                        │
└─────────────────────────────────────┘
```

---

# SLIDE 38 : ORCHESTRATION - APACHE AIRFLOW

**Apache Airflow :**
- DAGs (Directed Acyclic Graphs)
- Scheduling flexible
- Monitoring intégré
- Extensible avec plugins
- Interface web complète
- Standard de l'industrie

**Concepts :**
- DAG : Workflow défini
- Task : Étape du workflow
- Operator : Type de tâche
- Scheduler : Exécution automatique

---

# SLIDE 39 : CONTAINERS - DOCKER

**Docker :**
- Containerisation standard
- Portabilité complète
- Isolation des applications
- Facile à utiliser
- Écosystème riche

**Avantages :**
- "Ça marche sur ma machine" → Résolu
- Déploiement simplifié
- Scalabilité
- Isolation

---

# SLIDE 40 : ORCHESTRATION CONTAINERS - KUBERNETES

**Kubernetes :**
- Orchestration de containers
- Auto-scaling
- Haute disponibilité
- Gestion du load balancing
- Standard de l'industrie

**Concepts :**
- Pod : Plus petit déploiement
- Service : Point d'accès stable
- Deployment : Gestion des pods
- ReplicaSet : Réplication

---

# SLIDE 41 : CI/CD - GITHUB ACTIONS

**GitHub Actions :**
- Intégration GitHub native
- Automatisation complète
- Gratuit pour open source
- Nombreux templates
- Facile à configurer

**Workflow typique :**
```
Code → Tests → Build → Deploy
```

---

# SLIDE 42 : SCHÉMA D'ORCHESTRATION

```
┌─────────────────────────────────────┐
│   CODE SOURCE (Git Repository)      │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   CI/CD PIPELINE                    │
│                                     │
│   ┌──────┐  ┌──────┐  ┌──────┐    │
│   │Tests │→ │Build │→ │Deploy│    │
│   └──────┘  └──────┘  └──────┘    │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   PRODUCTION                        │
│                                     │
│   ┌──────────────┐                 │
│   │ Kubernetes   │                 │
│   │   / Docker   │                 │
│   └──────────────┘                 │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│   MONITORING                        │
│   - Prometheus                      │
│   - Grafana                        │
└─────────────────────────────────────┘
```

---

# SLIDE 43 : CRITÈRES DE SÉLECTION - VOLUME

**Petit volume (< 1GB) :**
- Pandas pour traitement
- SQLite pour stockage
- Jupyter pour analyse
- Pas besoin de distribution

**Volume moyen (1GB - 1TB) :**
- PostgreSQL/MySQL pour stockage
- Pandas ou Dask pour traitement
- Outils BI légers (Metabase, Superset)

**Grand volume (> 1TB) :**
- Spark pour traitement
- Data Warehouse (Snowflake, BigQuery)
- Outils distribués nécessaires

---

# SLIDE 44 : CRITÈRES DE SÉLECTION - VÉLOCITÉ

**Batch (traitement par lots) :**
- Spark pour gros volumes
- Airflow pour orchestration
- Exécution périodique (quotidienne, hebdomadaire)

**Real-time (temps réel) :**
- Kafka pour messaging
- Flink pour stream processing
- Traitement continu

**Exemple batch :** Rapport quotidien des ventes
**Exemple real-time :** Détection de fraude en temps réel

---

# SLIDE 45 : CRITÈRES DE SÉLECTION - BUDGET

**Open source (gratuit) :**
- PostgreSQL, Spark, Airflow
- Superset, Metabase, Grafana
- Scikit-learn, TensorFlow

**Commercial (payant) :**
- Snowflake, Tableau, Power BI
- Support et maintenance inclus
- Fonctionnalités avancées

**Conseil :** Commencer par open source, passer au commercial si besoin

---

# SLIDE 46 : CRITÈRES DE SÉLECTION - COMPÉTENCES

**Équipe Python :**
- Pandas, Scikit-learn
- Airflow, dbt
- Jupyter, Plotly

**Équipe SQL :**
- dbt, Data Warehouses
- Superset, Metabase
- SQL avancé

**Équipe No-code :**
- Power BI, Tableau
- AutoML
- Interfaces graphiques

---

# SLIDE 47 : MATRICE DE DÉCISION

| Besoin | Petit projet | Moyen projet | Grand projet |
|--------|--------------|--------------|--------------|
| Stockage | SQLite / PostgreSQL | PostgreSQL / MySQL | Data Warehouse |
| Traitement | Pandas | Spark / Dask | Spark / Flink |
| Analyse | Jupyter / Python | Superset / Metabase | Tableau / Power BI |
| ML | Scikit-learn | Scikit-learn / XGBoost | TensorFlow / PyTorch |
| Orchestration | Scripts Python | Airflow | Airflow / Kubeflow |

---

# SLIDE 48 : BONNES PRATIQUES - VERSIONING

**Code :**
- Utiliser Git
- Branches pour features
- Commits descriptifs
- Pull requests pour reviews

**Données :**
- DVC (Data Version Control)
- Snapshot des données importantes
- Traçabilité des versions

**Modèles :**
- MLflow pour versioning
- Tags et métadonnées
- Reproducibilité

---

# SLIDE 49 : BONNES PRATIQUES - DOCUMENTATION

**Code :**
- README complet
- Docstrings pour fonctions
- Commentaires pour logique complexe

**Pipelines :**
- Documentation des étapes
- Schémas d'architecture
- Guide d'utilisation

**Modèles :**
- Documentation des features
- Explication des choix
- Résultats et métriques

---

# SLIDE 50 : BONNES PRATIQUES - TESTING

**Tests unitaires :**
- Tester chaque fonction
- Couverture de code élevée
- Tests automatisés

**Tests d'intégration :**
- Tester les pipelines complets
- Validation des données
- Tests de performance

**Tests de données :**
- Validation des schémas
- Détection d'anomalies
- Tests de qualité

---

# SLIDE 51 : BONNES PRATIQUES - MONITORING

**Logs :**
- Logs structurés (JSON)
- Niveaux de log appropriés
- Centralisation des logs

**Métriques :**
- Métriques business
- Métriques techniques
- Dashboards de monitoring

**Alertes :**
- Alertes sur erreurs critiques
- Alertes sur anomalies
- Notification appropriée

---

# SLIDE 52 : ARCHITECTURE RECOMMANDÉE

```
┌─────────────────────────────────────────┐
│      SOURCES DE DONNÉES                 │
│  (APIs, Bases de données, Fichiers)     │
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│      INGESTION (ETL/ELT)                 │
│  (Airflow, NiFi, Scripts)                │
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│   STOCKAGE (Data Lake / Warehouse)     │
│  (S3, HDFS, Snowflake, BigQuery)        │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌──────────────┐
│  TRAITEMENT  │  │   ANALYSE    │
│  (Spark,     │  │  (BI Tools,  │
│   Pandas)    │  │   Python)    │
└──────┬───────┘  └──────┬───────┘
       │                 │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │ MACHINE LEARNING│
       │ (MLflow,        │
       │  Kubeflow)      │
       └─────────────────┘
```

---

# SLIDE 53 : CHECKLIST DE PROJET

Avant de démarrer un projet de données :

- [ ] Architecture définie et documentée
- [ ] Outils sélectionnés selon le contexte
- [ ] Environnement de développement configuré
- [ ] Pipeline de données fonctionnel
- [ ] Tests implémentés et passants
- [ ] Documentation complète
- [ ] Monitoring en place
- [ ] Plan de déploiement défini
- [ ] Plan de backup et recovery
- [ ] Sécurité et conformité vérifiées

---

# SLIDE 54 : RESSOURCES ET DOCUMENTATION

**Documentation officielle :**
- Apache Spark : spark.apache.org/docs/
- Pandas : pandas.pydata.org/docs/
- Apache Airflow : airflow.apache.org/docs/
- dbt : docs.getdbt.com/

**Communautés :**
- Stack Overflow
- GitHub Discussions
- Reddit (r/dataengineering, r/MachineLearning)

**Cours en ligne :**
- DataCamp
- Coursera
- Udacity

---

# SLIDE 55 : POINTS CLÉS À RETENIR

1. **Pas de solution unique**
   - Chaque contexte nécessite des outils adaptés
   - Évaluez vos besoins avant de choisir

2. **Écosystème ouvert**
   - Beaucoup d'outils open source de qualité
   - Gratuits et performants

3. **Évolution rapide**
   - Rester à jour avec les nouvelles technologies
   - Apprendre continuellement

4. **Pratique essentielle**
   - La théorie doit être complétée par la pratique
   - Expérimentez avec les outils

---

# SLIDE 56 : PROCHAINES ÉTAPES

1. **Compléter les exercices pratiques**
   - 7 exercices progressifs
   - Outils open source réels
   - Instructions détaillées

2. **Expérimenter avec différents outils**
   - Tester plusieurs solutions
   - Comparer les approches
   - Trouver vos préférences

3. **Construire un projet complet**
   - Intégrer plusieurs outils
   - Créer un pipeline end-to-end
   - Documenter votre travail

4. **Partager et collaborer**
   - Contribuer aux projets open source
   - Partager vos expériences
   - Apprendre de la communauté

---

# SLIDE 57 : EXERCICES PRATIQUES

**Exercice 01 : Apache Superset**
- Business Intelligence open source
- Création de dashboards

**Exercice 02 : Metabase**
- Self-Service BI
- Questions interactives

**Exercice 03 : ELK Stack**
- Analyse de logs avec Kibana

**Exercice 04 : Apache Spark**
- Traitement Big Data

**Exercice 05 : Grafana + Prometheus**
- Monitoring complet

**Exercice 06 : Apache Airflow**
- Orchestration de workflows

**Exercice 07 : dbt**
- Transformation SQL moderne

---

# SLIDE 58 : COMMENT UTILISER CE DÉPÔT

1. **Consultez les slides**
   - PowerPoint ou HTML
   - Comprenez les concepts

2. **Faites les exercices dans l'ordre**
   - Commencez par l'exercice 01
   - Suivez les instructions du README
   - Générez les données nécessaires

3. **Soumettez vos solutions**
   - Créez un dossier avec votre nom
   - Poussez sur GitHub
   - Suivez les instructions détaillées

4. **Consultez les corrections**
   - Après avoir essayé
   - Mot de passe : Abidexercice123

---

# SLIDE 59 : CONSEILS POUR RÉUSSIR

**Organisation :**
- Travaillez régulièrement
- Faites les exercices dans l'ordre
- Prenez des notes

**Pratique :**
- Testez chaque étape
- Expérimentez avec les outils
- Ne pas hésiter à essayer

**Documentation :**
- Lisez les README attentivement
- Consultez la documentation officielle
- Cherchez dans les communautés

**Persévérance :**
- Les erreurs font partie de l'apprentissage
- Demandez de l'aide si besoin
- Continuez à pratiquer

---

# SLIDE 60 : MERCI POUR VOTRE ATTENTION

**Master 2 - Développement Informatique**

**Outils de la Data**

**Formateur : Abid Hamza**

Bon courage avec les exercices pratiques !

N'hésitez pas à poser vos questions sur le dépôt GitHub.

---


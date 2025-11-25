# Exercice 05 : Grafana + Prometheus - Monitoring complet

## 🎯 Objectifs

- Installer Grafana et Prometheus
- Configurer Prometheus pour collecter des métriques
- Créer des dashboards Grafana professionnels
- Configurer des alertes
- Maîtriser un stack de monitoring complet

## 📋 Prérequis

- Docker et Docker Compose
- 2GB RAM minimum

## 📦 Installation

### Avec Docker Compose

Créez un fichier `docker-compose.yml` :

```yaml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - prometheus

volumes:
  prometheus_data:
  grafana_data:
```

## 📊 Données

1. **Générez les métriques** :
   ```bash
   cd exercice-05
   python generer_metriques.py
   ```

2. **Créez un exporter simple** pour simuler des métriques :
   ```bash
   python exporter_metriques.py
   ```

## 🎓 Instructions

### Étape 1 : Configuration Prometheus

Créez `prometheus.yml` :

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'metriques'
    static_configs:
      - targets: ['host.docker.internal:8000']
```

### Étape 2 : Démarrer les services

```bash
docker-compose up -d
```

### Étape 3 : Vérifier Prometheus

1. **Accédez à Prometheus** : http://localhost:9090
2. **Testez une requête** : `up`
3. **Explorez les métriques disponibles**

### Étape 4 : Configuration Grafana

1. **Accédez à Grafana** : http://localhost:3000
2. **Identifiants** : admin/admin
3. **Ajoutez Prometheus comme source** :
   - Configuration > Data Sources
   - Add data source > Prometheus
   - URL : http://prometheus:9090
   - Save & Test

### Étape 5 : Créer des dashboards

Créez au moins 6 panneaux :

1. **Time Series** : CPU par serveur
2. **Gauge** : Utilisation mémoire
3. **Bar Chart** : Top serveurs par charge
4. **Stat** : Nombre total de requêtes
5. **Heatmap** : Distribution des latences
6. **Table** : Métriques par serveur

### Étape 6 : Alertes

1. **Créez des règles d'alerte** :
   - CPU > 80%
   - Mémoire < 10%
   - Disque > 90%

2. **Configurez les notifications**

## 📁 Structure attendue

```
exercice-05/
├── README.md (ce fichier)
├── docker-compose.yml
├── prometheus.yml
├── exporter_metriques.py
├── generer_metriques.py
└── solutions/
    └── votre-nom/
        ├── dashboard.json
        ├── screenshots/
        └── resultats.md
```

## ✅ Critères d'évaluation

- [ ] Prometheus et Grafana installés
- [ ] Métriques collectées
- [ ] Au moins 6 panneaux créés
- [ ] Alertes configurées
- [ ] Dashboard exporté
- [ ] Documentation complète

## 💡 Conseils

- Utilisez les variables de dashboard
- Organisez les panneaux par catégorie
- Testez les alertes
- Documentez vos requêtes PromQL

## 📚 Ressources

- Documentation Grafana : https://grafana.com/docs/
- Documentation Prometheus : https://prometheus.io/docs/
- PromQL : https://prometheus.io/docs/prometheus/latest/querying/basics/

## 🆘 Aide

Si vous êtes bloqué :
1. Vérifiez les logs Docker
2. Consultez la documentation
3. Ouvrez une issue sur le dépôt GitHub

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Générez les métriques** :
   ```bash
   cd exercice-05
   python generer_metriques.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Exportez votre dashboard** depuis Grafana
4. **Prenez des captures d'écran**
5. **Créez un fichier `resultats.md`**

6. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 05 - Votre Nom"
   git push origin main
   ```

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !

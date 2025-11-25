# Exercice 03 : ELK Stack (Elasticsearch, Logstash, Kibana) - Analyse de logs

## 🎯 Objectifs

- Installer et configurer l'ELK Stack
- Ingérer des données avec Logstash
- Indexer dans Elasticsearch
- Visualiser dans Kibana
- Maîtriser un stack d'analyse de données complet

## 📋 Prérequis

- Docker et Docker Compose
- 4GB RAM minimum
- Connaissances de base en JSON

## 📦 Installation

### Avec Docker Compose (Recommandé)

Créez un fichier `docker-compose.yml` :

```yaml
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
      - es_data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.11.0
    ports:
      - "5044:5044"
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on:
      - elasticsearch

volumes:
  es_data:
```

Lancez avec :
```bash
docker-compose up -d
```

## 📊 Données

1. **Générez des logs simulés** :
   ```bash
   cd exercice-03
   python generer_logs.py
   ```

## 🎓 Instructions

### Étape 1 : Configuration Logstash

Créez un fichier `logstash.conf` :

```ruby
input {
  file {
    path => "/usr/share/logstash/data/logs/*.log"
    start_position => "beginning"
    codec => "json"
  }
}

filter {
  date {
    match => [ "timestamp", "ISO8601" ]
  }
  
  mutate {
    convert => {
      "status_code" => "integer"
      "response_time" => "float"
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
```

### Étape 2 : Vérifier Elasticsearch

1. **Vérifiez qu'Elasticsearch fonctionne** :
   ```bash
   curl http://localhost:9200
   ```

2. **Vérifiez les indices créés** :
   ```bash
   curl http://localhost:9200/_cat/indices?v
   ```

### Étape 3 : Configuration Kibana

1. **Accédez à Kibana** : http://localhost:5601
2. **Configurez l'index pattern** :
   - Allez dans Stack Management > Index Patterns
   - Créez un pattern : `logs-*`
   - Sélectionnez `@timestamp` comme time field

### Étape 4 : Créer des visualisations dans Kibana

Créez au moins 5 visualisations :

1. **Line Chart** : Nombre de requêtes par heure
   - Metric : Count
   - Bucket : Date Histogram sur `@timestamp`

2. **Pie Chart** : Répartition par status code
   - Slice : Terms sur `status_code`

3. **Bar Chart** : Top 10 endpoints
   - X-axis : Terms sur `endpoint`
   - Y-axis : Count

4. **Metric** : Temps de réponse moyen
   - Metric : Average de `response_time`

5. **Data Table** : Requêtes avec erreurs (status >= 400)
   - Filtre : `status_code >= 400`
   - Colonnes : timestamp, endpoint, status_code, response_time

### Étape 5 : Créer un Dashboard

1. **Créez un dashboard** : "Monitoring Application"
2. **Ajoutez vos visualisations**
3. **Configurez les filtres** :
   - Filtre temporel
   - Filtre par status code
   - Filtre par endpoint

### Étape 6 : Requêtes Elasticsearch

Testez des requêtes dans Dev Tools :

1. **Recherche simple** :
```json
GET /logs-*/_search
{
  "query": {
    "match": {
      "endpoint": "/api/users"
    }
  }
}
```

2. **Agrégation** :
```json
GET /logs-*/_search
{
  "size": 0,
  "aggs": {
    "status_codes": {
      "terms": {
        "field": "status_code"
      }
    }
  }
}
```

## 📁 Structure attendue

```
exercice-03/
├── README.md (ce fichier)
├── docker-compose.yml
├── logstash.conf
├── generer_logs.py
├── donnees/
│   └── logs/ (fichiers de logs)
└── solutions/
    └── votre-nom/
        ├── screenshots/
        ├── dashboard_export.json
        ├── resultats.md
        └── requetes_elasticsearch.md
```

## ✅ Critères d'évaluation

- [ ] ELK Stack installé et fonctionnel
- [ ] Logstash ingère les données
- [ ] Elasticsearch indexe correctement
- [ ] Au moins 5 visualisations créées dans Kibana
- [ ] Dashboard fonctionnel
- [ ] Documentation complète

## 💡 Conseils

- Commencez avec peu de données pour tester
- Utilisez Dev Tools pour tester les requêtes
- Explorez les différents types de visualisations
- Utilisez les filtres pour affiner vos analyses
- Documentez vos requêtes Elasticsearch

## 📚 Ressources

- Documentation ELK : https://www.elastic.co/guide/
- Guide Kibana : https://www.elastic.co/guide/en/kibana/current/index.html
- Guide Logstash : https://www.elastic.co/guide/en/logstash/current/index.html

## 🆘 Aide

Si vous êtes bloqué :
1. Vérifiez les logs des containers Docker
2. Consultez la documentation officielle
3. Ouvrez une issue sur le dépôt GitHub

## 📤 Comment soumettre votre solution

### Étapes pour pousser votre exercice sur GitHub

1. **Générez les logs** :
   ```bash
   cd exercice-03
   python generer_logs.py
   ```

2. **Créez votre dossier de solution** :
   ```bash
   mkdir -p solutions/votre-nom
   cd solutions/votre-nom
   ```

3. **Exportez votre dashboard** depuis Kibana
4. **Prenez des captures d'écran**
5. **Créez un fichier `resultats.md`**

6. **Ajoutez et commitez** :
   ```bash
   git add solutions/votre-nom/
   git commit -m "Solution exercice 03 - Votre Nom"
   git push origin main
   ```

**Important** : N'oubliez pas de remplacer "votre-nom" par votre vrai nom !

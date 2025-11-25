# M2 DI - Outils de la Data

Ce dépôt contient les ressources pédagogiques pour le cours **Outils de la Data** du Master 2 en Data Intelligence.

## 📚 Contenu

- **Slides de cours** : Présentation complète sur les outils de la data
- **Exercices pratiques** : Exercices open source pour mettre en pratique les concepts
- **Ressources** : Documentation et liens utiles

## 🎯 Objectifs du cours

Ce cours vise à :
- Comprendre l'écosystème des outils de la data
- Maîtriser les outils essentiels pour le traitement et l'analyse de données
- Apprendre à choisir les bons outils selon le contexte
- Mettre en pratique les concepts à travers des exercices

## 📁 Structure du dépôt

```
.
├── slides/              # Présentations du cours
│   ├── index.html       # Présentation principale (Reveal.js)
│   └── assets/          # Images, schémas, diagrammes
├── exercices/           # Exercices pratiques
│   ├── exercice-01/     # Premier exercice
│   ├── exercice-02/     # Deuxième exercice
│   └── ...
├── ressources/          # Documentation et ressources
└── README.md            # Ce fichier
```

## 🚀 Démarrage rapide

### Visualiser les slides

1. Ouvrir `slides/index.html` dans un navigateur web
2. Utiliser les flèches pour naviguer entre les slides
3. Appuyer sur `F` pour le mode plein écran

### Exécuter les exercices

Chaque exercice contient :
- Un fichier `README.md` avec les instructions
- Le code source nécessaire
- Les données d'exemple (si nécessaire)

## 🛠️ Technologies utilisées

- **Reveal.js** : Pour les présentations interactives
- **Python** : Pour les exercices pratiques
- **Jupyter Notebook** : Pour certains exercices interactifs

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📤 Comment soumettre vos réponses aux exercices

### Méthode 1 : Fork et Pull Request (Recommandé)

1. **Forker le dépôt** :
   - Cliquez sur le bouton "Fork" en haut à droite de cette page
   - Cela crée une copie du dépôt dans votre compte GitHub

2. **Cloner votre fork** :
   ```bash
   git clone https://github.com/VOTRE_USERNAME/M2_DI_Outils-de-la-data.git
   cd M2_DI_Outils-de-la-data
   ```

3. **Créer une branche pour votre travail** :
   ```bash
   git checkout -b nom-prenom-exercice-01
   # Exemple : git checkout -b jean-dupont-exercice-01
   ```

4. **Travailler sur l'exercice** :
   - Allez dans le dossier de l'exercice (ex: `exercices/exercice-01/`)
   - Créez un dossier avec votre nom : `exercices/exercice-01/solutions/votre-nom/`
   - Placez vos fichiers de solution dans ce dossier
   - Suivez les instructions dans le README de l'exercice

5. **Ajouter et commiter vos changements** :
   ```bash
   git add .
   git commit -m "Solution exercice 01 - Votre Nom"
   ```

6. **Pousser vers votre fork** :
   ```bash
   git push origin nom-prenom-exercice-01
   ```

7. **Créer une Pull Request** :
   - Allez sur votre fork sur GitHub
   - Cliquez sur "Compare & pull request"
   - Remplissez le formulaire avec votre nom et le numéro de l'exercice
   - Soumettez la Pull Request

### Méthode 2 : Ajout direct dans le dépôt (si vous avez les droits)

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/AbidHamza/M2_DI_Outils-de-la-data.git
   cd M2_DI_Outils-de-la-data
   ```

2. **Créer votre dossier de solution** :
   - Créez un dossier dans `exercices/exercice-XX/solutions/votre-nom/`
   - Placez vos fichiers de solution dedans

3. **Pousser vos changements** :
   ```bash
   git add .
   git commit -m "Solution exercice XX - Votre Nom"
   git push origin main
   ```

### Structure de soumission attendue

Pour chaque exercice, créez un dossier avec votre nom dans le dossier `solutions/` :

```
exercices/
└── exercice-01/
    ├── README.md
    ├── donnees/
    └── solutions/
        ├── jean-dupont/
        │   ├── solution.py
        │   ├── resultats.md
        │   └── README.md (optionnel - explication de votre approche)
        └── marie-martin/
            ├── solution.py
            └── resultats.md
```

### 📋 Checklist avant de soumettre

- [ ] J'ai lu et compris les instructions de l'exercice
- [ ] Mon code est commenté et lisible
- [ ] J'ai testé mon code et il fonctionne
- [ ] J'ai créé un dossier avec mon nom dans `solutions/`
- [ ] J'ai ajouté un fichier `resultats.md` ou `README.md` expliquant ma solution
- [ ] Mon commit message est clair et contient mon nom

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Proposer de nouveaux exercices
- Améliorer la documentation
- Corriger les erreurs

## 📧 Contact

Pour toute question, ouvrez une issue sur ce dépôt.


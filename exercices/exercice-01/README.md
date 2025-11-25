# Exercice 01 : Manipulation de données avec Pandas

## 🎯 Objectifs

- Maîtriser les opérations de base avec Pandas
- Apprendre à nettoyer et transformer des données
- Créer des visualisations simples

## 📋 Prérequis

- Python 3.8+
- Bibliothèques : pandas, matplotlib, numpy

## 📦 Installation

```bash
pip install pandas matplotlib numpy
```

## 📊 Données

Les données se trouvent dans le dossier `donnees/`. Vous devez utiliser le fichier `ventes.csv` qui contient des données de ventes d'une entreprise.

## 🎓 Instructions

### Étape 1 : Chargement des données

1. Créez un script Python `solution.py` dans votre dossier de solution
2. Chargez le fichier `ventes.csv` avec pandas
3. Affichez les 5 premières lignes
4. Affichez les informations générales sur le DataFrame (types, valeurs manquantes, etc.)

### Étape 2 : Nettoyage des données

1. Identifiez et traitez les valeurs manquantes
2. Vérifiez les doublons et supprimez-les si nécessaire
3. Convertissez les colonnes de dates au bon format si nécessaire
4. Vérifiez les types de données et corrigez-les si besoin

### Étape 3 : Analyse exploratoire

1. Calculez les statistiques descriptives (moyenne, médiane, écart-type)
2. Identifiez les 10 meilleurs produits en termes de ventes
3. Calculez le chiffre d'affaires total par mois
4. Trouvez le mois avec le plus de ventes

### Étape 4 : Visualisation

1. Créez un graphique en barres montrant le chiffre d'affaires par mois
2. Créez un graphique en camembert (pie chart) pour la répartition des ventes par catégorie
3. Sauvegardez les graphiques dans votre dossier de solution

### Étape 5 : Export des résultats

1. Créez un fichier `resultats.md` qui contient :
   - Un résumé de votre analyse
   - Les principales découvertes
   - Les statistiques clés
   - Les graphiques générés (références aux fichiers images)

## 📁 Structure attendue

```
exercice-01/
├── README.md (ce fichier)
├── donnees/
│   └── ventes.csv
└── solutions/
    └── votre-nom/
        ├── solution.py
        ├── resultats.md
        ├── graphique_ventes_mois.png
        └── graphique_categories.png
```

## ✅ Critères d'évaluation

- [ ] Code fonctionnel et sans erreurs
- [ ] Code bien commenté et organisé
- [ ] Toutes les étapes sont complétées
- [ ] Les visualisations sont claires et pertinentes
- [ ] Le fichier `resultats.md` est complet et bien structuré

## 💡 Conseils

- Utilisez `df.info()` et `df.describe()` pour explorer vos données
- N'hésitez pas à utiliser `df.head()`, `df.tail()`, `df.sample()` pour inspecter les données
- Pour les graphiques, utilisez `plt.savefig()` pour sauvegarder
- Documentez votre code avec des commentaires

## 🆘 Aide

Si vous êtes bloqué :
1. Consultez la documentation Pandas : https://pandas.pydata.org/docs/
2. Ouvrez une issue sur le dépôt GitHub
3. Consultez les ressources dans le dossier `ressources/`

## 📤 Soumission

Suivez les instructions dans le README principal du dépôt pour soumettre votre solution.


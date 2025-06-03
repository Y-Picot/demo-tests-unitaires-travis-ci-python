# Démonstration Tests Unitaires et Travis CI avec Python

[![Tests](https://github.com/Y-Picot/demo-tests-unitaires-travis-ci-python/actions/workflows/tests.yml/badge.svg)](https://github.com/Y-Picot/demo-tests-unitaires-travis-ci-python/actions/workflows/tests.yml)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Projet de démonstration pour apprendre l'intégration continue avec Travis CI et GitLab CI en utilisant des tests unitaires Python. Ce projet utilise une bibliothèque de calculs mathématiques simples comme exemple pratique pour illustrer les bonnes pratiques de CI/CD.

## 🎯 Objectif pédagogique

Ce projet a été créé pour apprendre et démontrer :
- **Tests unitaires Python** avec unittest
- **Intégration continue** avec Travis CI
- **Pipeline CI/CD** avec GitLab CI
- **GitHub Actions** pour l'automatisation des tests
- **Bonnes pratiques** de développement Python
- **Documentation** de projet open-source

### Contenu de la démonstration
- **Bibliothèque exemple** : fonctions mathématiques simples
- **Tests complets** : couverture de toutes les fonctions
- **Configuration CI** : Travis CI, GitLab CI et GitHub Actions prêts à l'emploi

## 🛠️ Technologies utilisées

- **Langage** : Python 3.8+
- **Tests** : unittest (bibliothèque standard)
- **Intégration Continue** :
  - Travis CI
  - GitLab CI
  - GitHub Actions
- **Documentation** : Docstrings conformes PEP 257

## 📋 Prérequis

- Python 3.8 ou version supérieure
- Aucune dépendance externe (utilise uniquement les bibliothèques standard)

## 🚀 Installation

### Clonage du dépôt
```bash
git clone https://github.com/Y-Picot/demo-tests-unitaires-travis-ci-python.git
cd demo-tests-unitaires-travis-ci-python
```

### Vérification de l'installation
```bash
python main.py
```

## 💻 Exemples d'utilisation

### Utilisation basique
```python
import bibliotheque

# Opérations arithmétiques
resultat_addition = bibliotheque.addition(5, 3)        # Retourne 8
resultat_division = bibliotheque.division(10, 2)       # Retourne 5.0

# Fonctions mathématiques avancées
carre = bibliotheque.carree(4)                         # Retourne 16
racine = bibliotheque.racineCarree(25)                 # Retourne 5.0
cosinus = bibliotheque.cosinus(0)                      # Retourne 1.0
```

### Démonstration complète
```bash
python main.py
```

### Exécution des tests
```bash
python -m unittest unitTests.py -v
```

## 📁 Structure du projet

```
demo-tests-unitaires-travis-ci-python/
├── bibliotheque.py          # Bibliothèque exemple avec fonctions mathématiques
├── main.py                 # Démonstration d'utilisation
├── unitTests.py            # Tests unitaires complets  
├── README.md              # Documentation du projet
├── LICENSE                # Licence MIT
├── .gitignore             # Fichiers à ignorer par Git
├── .travis.yml            # Configuration Travis CI
├── .gitlab-ci.yml         # Configuration GitLab CI
└── .github/
    └── workflows/
        └── tests.yml      # Configuration GitHub Actions
```

## 🧪 Tests

Le projet inclut une suite de tests complète couvrant :
- Toutes les fonctions mathématiques
- Gestion des cas limites (division par zéro)
- Validation des résultats numériques

```bash
# Exécuter tous les tests
python -m unittest unitTests.py

# Exécuter avec verbosité
python -m unittest unitTests.py -v
```

## 🤝 Guide de contribution

1. **Fork** ce dépôt
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalite`)
3. **Commitez** vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. **Pushez** vers la branche (`git push origin nouvelle-fonctionnalite`)
5. **Créez** une Pull Request

### Standards de code
- Suivre les conventions PEP 8
- Ajouter des docstrings pour toutes les fonctions
- Inclure des tests pour toute nouvelle fonctionnalité
- Maintenir la couverture de tests à 100%

## 🔗 Liens utiles

- [Documentation Python unittest](https://docs.python.org/3/library/unittest.html)
- [Travis CI Documentation](https://docs.travis-ci.com/)
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)

---

**Version actuelle** : 1.0.0

## 📄 Licence

Licence MIT - voir [LICENSE](LICENSE) pour les détails.

## 👤 Auteur

**Y-Picot** - [GitHub](https://github.com/Y-Picot)

---

⭐ Projet utile ? N'hésitez pas à lui donner une étoile !

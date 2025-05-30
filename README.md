# Bibliothèque de Calculs Mathématiques

[![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://shields.io/)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Une bibliothèque Python simple et efficace pour effectuer des calculs mathématiques de base et des opérations trigonométriques. Ce projet démontre l'utilisation des tests unitaires et de l'intégration continue avec Travis CI et GitLab CI.

## 📋 Résumé du projet

Cette bibliothèque fournit un ensemble de fonctions mathématiques essentielles :
- **Opérations arithmétiques** : addition, soustraction, multiplication, division
- **Fonctions avancées** : carré, racine carrée, cosinus
- **Gestion des erreurs** : division par zéro sécurisée
- **Tests complets** : couverture de toutes les fonctions avec unittest

## 🛠️ Technologies utilisées

- **Langage** : Python 3.8+
- **Tests** : unittest (bibliothèque standard)
- **Intégration Continue** :
  - Travis CI
  - GitLab CI
- **Documentation** : Docstrings conformes PEP 257

## 📋 Prérequis

- Python 3.8 ou version supérieure
- Aucune dépendance externe (utilise uniquement les bibliothèques standard)

## 🚀 Installation

### Clonage du dépôt
```bash
git clone https://github.com/Y-Picot/bibliotheque-calculs-mathematiques.git
cd bibliotheque-calculs-mathematiques
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
bibliotheque-calculs-mathematiques/
├── bibliotheque.py      # Bibliothèque principale avec toutes les fonctions
├── main.py             # Démonstration d'utilisation
├── unitTests.py        # Tests unitaires complets
├── README.md          # Documentation
├── LICENSE            # Licence MIT
├── .gitignore         # Fichiers à ignorer par Git
├── .travis.yml        # Configuration Travis CI
└── .gitlab-ci.yml     # Configuration GitLab CI
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

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteur

- **Y-Picot** - Développeur principal

## 🔗 Liens utiles

- [Documentation Python unittest](https://docs.python.org/3/library/unittest.html)
- [Travis CI Documentation](https://docs.travis-ci.com/)
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)

---

**Version actuelle** : 1.0.0
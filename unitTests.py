"""
Tests Unitaires pour la Bibliothèque de Calculs Mathématiques
============================================================

Ce module contient tous les tests unitaires pour vérifier le bon
fonctionnement des fonctions mathématiques de la bibliothèque.

Auteur: Y-Picot
Version: 1.0.0
"""

import unittest
import bibliotheque


class TestsCalculsMathematiques(unittest.TestCase):
    """
    Classe de tests pour toutes les fonctions mathématiques.
    
    Cette classe teste les opérations arithmétiques de base
    et les fonctions mathématiques avancées.
    """
    
    def setUp(self):
        """
        Prépare les données de test avant chaque test.
        
        Initialise les valeurs numériques utilisées dans les tests.
        """
        self.nombre_un = 1      # Premier nombre pour les tests
        self.nombre_deux = 2    # Deuxième nombre pour les tests  
        self.nombre_cinquante = 50   # Nombre pour test racine carrée
        self.nombre_zero = 0    # Zéro pour tester la division

    def tearDown(self):
        """
        Nettoie après chaque test.
        
        Remet les variables à None (optionnel en Python).
        """
        self.nombre_un = None
        self.nombre_deux = None 
        self.nombre_cinquante = None
        self.nombre_zero = None
        
    def test_addition(self):
        """Test de la fonction addition."""
        # Teste que 1 + 2 = 3
        self.assertEqual(3, bibliotheque.addition(self.nombre_un, self.nombre_deux))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(5, bibliotheque.addition(self.nombre_un, self.nombre_deux))        

    def test_soustraction(self):
        """Test de la fonction soustraction."""
        # Teste que 1 - 2 = -1
        self.assertEqual(-1, bibliotheque.soustraction(self.nombre_un, self.nombre_deux))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(4, bibliotheque.soustraction(self.nombre_un, self.nombre_deux))
    
    def test_multiplication(self):
        """Test de la fonction multiplication."""
        # Teste que 1 * 2 = 2
        self.assertEqual(2, bibliotheque.multiplication(self.nombre_un, self.nombre_deux))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(4, bibliotheque.multiplication(self.nombre_un, self.nombre_deux))
        
    def test_division(self):
        """Test de la fonction division."""
        # Teste que 1 / 2 = 0.5
        self.assertEqual(0.5, bibliotheque.division(self.nombre_un, self.nombre_deux))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(4, bibliotheque.division(self.nombre_un, self.nombre_deux))
        # Teste la division par zéro (doit retourner 0.0)
        self.assertEqual(0.0, bibliotheque.division(self.nombre_un, self.nombre_zero))
        
    def test_carree(self):
        """Test de la fonction carré."""
        # Teste que 2² = 4
        self.assertEqual(4, bibliotheque.carree(self.nombre_deux))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(1, bibliotheque.carree(self.nombre_deux))
   
    def test_racineCarree(self):
        """Test de la fonction racine carrée."""
        # Teste que √50 ≈ 7.07 (arrondi à 2 décimales)
        self.assertEqual(7.07, bibliotheque.racineCarree(self.nombre_cinquante))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(1, bibliotheque.racineCarree(self.nombre_cinquante))
    
    def test_cosinus(self):
        """Test de la fonction cosinus."""
        # Teste que cos(1) ≈ 0.54 (arrondi à 2 décimales)
        self.assertEqual(0.54, bibliotheque.cosinus(self.nombre_un))
        # Teste qu'il ne retourne pas une valeur incorrecte
        self.assertNotEqual(1, bibliotheque.cosinus(self.nombre_un))          


if __name__ == '__main__':
    # Lance tous les tests unitaires
    unittest.main()
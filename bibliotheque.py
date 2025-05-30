"""
Bibliothèque de Calculs Mathématiques
=====================================

Ce module fournit des fonctions mathématiques de base pour effectuer
des opérations arithmétiques et trigonométriques simples.

Auteur: Y-Picot
Version: 1.0.0
"""

import math


# ========================================
# FONCTIONS ARITHMÉTIQUES DE BASE
# ========================================

def addition(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float|int): Premier nombre
        b (float|int): Deuxième nombre
    
    Returns:
        float|int: La somme de a et b
    """
    return a + b


def soustraction(a, b):
    """
    Soustrait le deuxième nombre du premier.
    
    Args:
        a (float|int): Premier nombre (minuende)
        b (float|int): Deuxième nombre (soustracteur)
    
    Returns:
        float|int: La différence a - b
    """
    return a - b


def multiplication(a, b):
    """
    Multiplie deux nombres.
    
    Args:
        a (float|int): Premier facteur
        b (float|int): Deuxième facteur
    
    Returns:
        float|int: Le produit de a et b
    """
    return a * b


def division(a, b):
    """
    Divise le premier nombre par le deuxième.
    
    Args:
        a (float|int): Dividende
        b (float|int): Diviseur
    
    Returns:
        float: Le quotient de a / b, arrondi à 2 décimales
               Retourne 0.0 si division par zéro
    """
    resultat = 0.0
    if b != 0:
        resultat = round(a / b, 2)
    else:
        print("il ne faut pas diviser par 0")
    return resultat


def carree(a):
    """
    Calcule le carré d'un nombre.
    
    Args:
        a (float|int): Le nombre à élever au carré
    
    Returns:
        float|int: Le carré de a (a²)
    """
    return a * a


# ========================================
# FONCTIONS MATHÉMATIQUES AVANCÉES
# ========================================

def racineCarree(a):
    """
    Calcule la racine carrée d'un nombre.
    
    Args:
        a (float|int): Le nombre dont calculer la racine carrée (doit être positif)
    
    Returns:
        float: La racine carrée de a, arrondie à 2 décimales
    """
    return round(math.sqrt(a), 2)


def cosinus(a):
    """
    Calcule le cosinus d'un angle en radians.
    
    Args:
        a (float|int): L'angle en radians
    
    Returns:
        float: Le cosinus de a, arrondi à 2 décimales
    """
    return round(math.cos(a), 2)


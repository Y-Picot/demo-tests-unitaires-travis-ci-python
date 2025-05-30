"""
Démonstration de la Bibliothèque de Calculs Mathématiques
=========================================================

Ce fichier démontre l'utilisation des fonctions de la bibliothèque
mathématique en affichant des exemples de calculs.

Auteur: Y-Picot
Version: 1.0.0
"""

import bibliotheque


def main():
    """
    Fonction principale qui démontre l'utilisation de toutes les fonctions
    de la bibliothèque mathématique.
    """
    print("=== Démonstration de la Bibliothèque Mathématique ===\n")
    
    # Définition des valeurs de test
    premier_nombre = 1
    deuxieme_nombre = 2  
    nombre_pour_racine = 50
    diviseur_zero = 0
    
    print("Valeurs utilisées pour les démonstrations :")
    print(f"Premier nombre : {premier_nombre}")
    print(f"Deuxième nombre : {deuxieme_nombre}")
    print(f"Nombre pour racine carrée : {nombre_pour_racine}")
    print(f"Diviseur zéro : {diviseur_zero}\n")
    
    # Démonstration des opérations arithmétiques
    print("--- Opérations arithmétiques de base ---")
    print(f"Addition : {premier_nombre} + {deuxieme_nombre} = {bibliotheque.addition(premier_nombre, deuxieme_nombre)}")
    print(f"Soustraction : {premier_nombre} - {deuxieme_nombre} = {bibliotheque.soustraction(premier_nombre, deuxieme_nombre)}")
    print(f"Multiplication : {premier_nombre} × {deuxieme_nombre} = {bibliotheque.multiplication(premier_nombre, deuxieme_nombre)}")
    print(f"Division : {premier_nombre} ÷ {deuxieme_nombre} = {bibliotheque.division(premier_nombre, deuxieme_nombre)}")
    print(f"Division par zéro : {premier_nombre} ÷ {diviseur_zero} = {bibliotheque.division(premier_nombre, diviseur_zero)}")
    
    # Démonstration des fonctions mathématiques avancées
    print("\n--- Fonctions mathématiques avancées ---")
    print(f"Carré de {deuxieme_nombre} : {deuxieme_nombre}² = {bibliotheque.carree(deuxieme_nombre)}")
    print(f"Racine carrée de {nombre_pour_racine} : √{nombre_pour_racine} = {bibliotheque.racineCarree(nombre_pour_racine)}")
    print(f"Cosinus de {premier_nombre} radian : cos({premier_nombre}) = {bibliotheque.cosinus(premier_nombre)}")
    
    print("\n=== Fin de la démonstration ===")


if __name__ == '__main__':
    # Exécute la démonstration si le fichier est lancé directement
    main()
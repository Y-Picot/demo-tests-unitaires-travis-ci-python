#import
import math

#Fonctions
def addition(a, b):
    return a+b

def soustraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b): 
    resultat = 0.0
    if b != 0:
       resultat = round(a/b,2)
    else:
        print("il ne faut pas diviser par 0")
    return resultat

def carree(a):
    return a*a

#Math
def racineCarree(a):
    return round(math.sqrt(a),2)

def cosinus(a):
    return round(math.cos(a),2)


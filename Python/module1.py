def transformation(liste):
    for ind in range(0,5):
        ind*liste[ind]
    return liste
"""Exercice 1"""

def trandsformation1(liste):
    for indice in range(0,5):
        liste[indice]=indice*liste[indice]
    return liste

"""Exercice 2"""

def transformation2(liste):
    tab=[]
    for indice in range(0,5):
        valeur=indice*liste[indice]
        tab.append(valeur)
    return tab

"""Exercice 3"""

#Il s'agit d'une épreuve de Bernoulli de paramètre n et p=0,3.

"""Exercice 4"""

from random import random
def nombre_succés():
    liste=[]
    for nb in range(0,10):
        if random()<0.75:
            liste.append("S")
        else:
            liste.append("E")
    return liste

"""Exercice 5"""

from random import random
def nombre_succés2(n,p):
    liste=[]
    for nb in range(n):
        if random()<p:
            liste.append("S")
        else:
            liste.append("E")
    return liste








from __future__ import print_function
#Imane OUBALID: Une jeune marocaine, titulaire d'un master en  Réseaux et Systèmes Informatique. 
#Elle dispose d'un esprit d'analyse, de synthèse, d'une capacité d'adaptation aux nouvelles situations, 
#et elle est passionnée par la programmation et les nouvelles technologies.


#Booleen est un type de donnees qui ne peut prendre que deux valeurs logique: vrai (True) ou faux (False)
#Il utilise d'autre expression tell que: et(and) non(not) ou(or)
#A note il faut respecter l'ecriture des mots clea = 6

#voila un exemple simple d'expressions booleennes
A = 6
print((A == 7)) #renvoie la valeur logique False
print((A == 6)) #True

#l'utilisation de l'operateur non(not) renvoie l'oppose de la valeur
print('************ Operateur: not *************')
B = True
C = False
print((not B)) # resultat sera l'oppose de la valeur logique True = False(faux)
print((not not B))#True
print((not C))#True

#l'operateur and(et) renvoie Vrai si tous les valeurs sont vraies 
print('************ Operateur: And *************')
print((True and True)) #True
print((True and False)) #False
print((False and True)) #False
print((False and False)) #False

D = 8
E = 9
print((D == 8 and D==9))#False
print((E == 9 and D==8))#True
print((not D and E==9))#False

#l'operateur or(ou) renvoie Vrai si ou moins une valeur est vraie
print('************ Operateur: or *************')
print((True or True)) #True
print((True or False)) #True
print((False or True)) #True
print((False or False)) #False

F=3
G=5
print((F==3 or F==0))#True
print((F==0 or G==0))#False
print((not F==0 or G==0))#True




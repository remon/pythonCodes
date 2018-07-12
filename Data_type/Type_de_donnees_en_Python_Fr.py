#Il existe de nombreux types predefinis en Python 
#Nombre:  Il y a trois types numeriques en Python : Le type entier (int), Le type flottant (float), Le type complexe (complex )
print "******Types numeriques*******"
print "1:", type(1)
print "1,345:",type(1.345)
print "2j:",type(2j)

print "******Booleen*******"
#Booleen: est un type de donnees qui ne peut prendre que deux valeurs logique: Vrai(True) et Faux(False)
print "Vrai ou Faux:", type(True)

print "******Chaines de caracteres*******"
#Chaine de caracteres( str ): est une suite de caracteres non modifiable.
chaine="Hello"
print chaine, type("chaine")

print "******Listes*******"
#liste:est une suite modifiable de donnees.
liste=[1,3,'a', '',0]
print liste, type(liste)

print "******Tuples*******"
#Tuple: suite non modifiable de donnees.
tuple=(1,'a','',7,'b')
print tuple, type(tuple)

print "******Ensembles*******"
#Ensemble:(set) est une collection modifiable de donnees sans ordre defini et sans doublons
ensemble ={1,'','a','b',2,4,2,'a'}
print ensemble, type(ensemble)

print "******Dictionnaire*******"
#Dictionnaire: est une collection modifiable de couples(Cle,valeur)sans ordre defini et sans doublons de cles
dictionnaire={7:1,'i':2, 4:1,'a':1, 7:1,'m':3}
print dictionnaire, type(dictionnaire)

"""Conversion
Il est possible de convertir explicitement une donnee d'un type vers un autre, 
en utilisant des fonctions predefinies."""
a = 234
print a, type(a)
a= float(a)
print a, type(a)
a= str(a)
print a, type(a)
a= set(a)
print a, type(a)
a= bool(a)
print a, type(a)
"""la fonction print() permet l'affichage a l'ecran des resultats d'une operation effectuee par le programme
il peut s'agir d'une chaine de caracteres, d'un nombre, du resultat d'un calcul, etc..."""

print("Bonjour")#affichage d'une chaine de caracteres
print(True)#Affichage d'un booleen
print(12)#affichage d'un entier
x=3
y=4
print(x+y)#Calcul de deux variables x et y
print(9%6)#Calcul
L=[2,'R',45]
print(L)

Nom="Mark"
ville="Toulouse"
age=25
print ("Je m'appelle",Nom , "j'ai",age,"ans et j'habite a",ville)

#Fonction format(): s'affranchit des contraintes des guillemets et des signes de concatenation
print("Je m'appelle {0} , j'ai {1} ans et j'habite a la {0}" .format("France", 25))

#concatenation avec le signe %
a=3
b=2.4
c="abc"
print("a=%d, b=%f, c=%s " %(a, b, c))
"""la fonction: print comme son nom l'indique, elle affiche quelque chose a l'ecran mais qui ne retourne rien.
a l'inverse 'return' est un mot cle du langage python qui presente ce que la fonctionne renvoi."""

def f_r(x):
	return x

print ("*****Appel de la fonction*****")
f_r(6)#Appel de la fonction f_r(x) qui renvoie la valeur de x (sans affichage)
print ("**********Affichage***********")
print(f_r(6))#print affiche la valeur renvoie par la fonction f_r(x)

def f_p(x):
	print(x)

print ("*****Appel de la fonction*****")
f_p(5)#appel de la fonction f_p(x) qui affiche la valeur de x
print ("**********Affichage***********")
print(f_p(5)) 


def f_rp(x):
	return x
	print (x)

print ("*****Appel de la fonction*****")
f_rp(4)
print ("**********Affichage***********")
print (f_rp(4))

def f_pr(x):
	print (x)
	return x

print ("*****Appel de la fonction*****")
f_pr(3)
print ("**********Affichage***********")
print (f_pr(3))
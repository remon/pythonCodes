#example 2
#added by @sagarbabalsure 
#This example is like guess game.Where user try to guess the randomly generated number in three trials.


import string
import random
from random import randint
x = randint(1, 100)
print(x)
count=3
while count>0:
	y=int(input("Enter your guess: "))
	count=count-1
	if x==y:
		print("Oh..your guess is correct")
	else:
		print("you have %d guesses remaining" %(count))
		if count==0:
			print("sorry you lose")
	

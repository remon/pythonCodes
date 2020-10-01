import random
import time
print("Lets play guessing game:\n")
n=int(random.randint(1,30))
time.sleep(1)
print("i have choosen my no \n ")
print("guess my selected no")
p,chance=0,9
while p!=n and chance>0:
    p=int(input())
    if p<n:
        print("Add me")
        chance-=1
    elif p>n:
        print("Decrease  ME")
        chance-=1
    elif p==n:
        print("Wohooo! You are An IQ master")
        break

    print('You have {} chances left'.format(chance))
if chance==0:
    print("You Loose the game")

    
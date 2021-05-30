#what is the output of this code?
gun = lambda x:x*x
data = 1
for i in range(1,3):
   data+=gun(i)
print(gun(data))

#the out put is 36 because data is 6 and 6 times 6 equals 36
#Why not make it harder by doing this

for i in range(2,7):
   gun(gun(data))
   
print(data)

#LOL I'm wierd

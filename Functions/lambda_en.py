#what is the output of this code?
#lamda functions are single line functions, they can also be used without name as anonymous functions

gun = lambda x:x*x # gun stores the function
data = 1
for i in range(1,3):
   data+=gun(i)
print(gun(data))


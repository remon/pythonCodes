from __future__ import print_function
#Syntax
#def function_name( parameters ):     ==>parameters means passing argument to function
#block of code
#retrun or print

print ("Example 1")
def names(x):
    print(x)
names("dima")
print ("----------------")


print ("Example 2")
def emplpyee_name():
    name=["Sara","Ahmad","Dima","Raed","Wael"]
    return name
print(emplpyee_name())
print ("----------------")

print ("Example 3")
def sum(x,y):
    s = x + y
    return s
print(sum(3,4))
print ("----------------")

print ("Example 4")
def sum(x,y=6):
    s = x + y
    return s
print(sum(3))
print ("----------------")

#added by @engshorouq
#example 5
print("Example 5 ")
def extend_list(val,my_list=[]):
    my_list.append(val)
    return my_list
print(extend_list('first iteam'))
print(extend_list('second iteam in same list'))
print(extend_list("new list",[]))    





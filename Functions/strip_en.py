#strip() returns a copy of the string
#in which all chars have been stripped
#from the beginning and the end of the string

#lstrip() removes leading characters (Left-strip)
#rstrip() removes trailing characters (Right-strip)




#Syntax
#str.strip([chars]);

#Example 1
#print Python a high level  
str = "Python a high level language";
print str.strip( 'language' )

#Examlpe 2
str = "Python a high level language , Python")

#print a high level language , 
print str.strip("Python")
#print a high level language , Python
print str.lstrip("Python")
#print Python a high level language , 
print str.rstrip("Python")


# Examples on how to uses python Assignments operators 
'''
Assignment operators means:
adding a new value to variable
like increase value / decrease / multiply and more
we usually use this kind of assignments in loops or condition statements
''' 
a = 2 ; b = 1 ; c = 0
print "values = ", "a=" , a , "b=" ,  b , "c=" , c 

# Addition or Subtraction c = c + a / c = c - b
c += a
print "Add c value by a =" , c
c -= b
print "Subtract c value by b =" , c

# multiply c = c * a 
c *= a
print "multiply c value by a =" , c

# Divide  c = c / a 
c /= a
print "Divide c value by a = " , c

# Mod of dividing c by a , c = c % a 
c  %= a 
print "Mod c value by a = " , c

# Exponent or power c by a , c = c ** a 
c **= a
print "power c value by = " , c

# floor Division or integer division c = c // a  
c //= a
print "Integer Division c value by a = " , c

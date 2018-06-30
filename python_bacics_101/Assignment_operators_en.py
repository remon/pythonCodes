# Examples on how to uses python Assignments operators 
'''
Assignment operators means:
adding a new value to variable , ike increase value / decrease / multiply and more

		Operator 	| Description
	------------------------------------------
	= equal		 	| Assigns values from right side operands to left side operand for example: a = 10 or c = a + b assigns value of a + b into c
	+= Add AND		| It adds right operand to the left operand and assign the result to left operand
	-= Subtract AND 	| It subtracts right operand from the left operand and assign the result to left operand
	*= Multiply AND		| It multiplies right operand with the left operand and assign the result to left operand
	/= Divide AND		| It divides left operand with the right operand and assign the result to left operand
	%= Modulus AND		| It takes modulus using two operands and assign the result to left operand
	**= Exponent AND	| Performs exponential (power) calculation on operators and assign value to the left operand
	//= Floor Division	| It performs floor division on operators and assign value to the left operand

when do we use it ? 
we usually use this kind of assignments in loops or condition statements
''' 
from __future__ import print_function

a = 2 ; b = 1 ; c = 0
print("values = ", "a=" , a , "b=" ,  b , "c=" , c) 

# Addition or Subtraction c = c + a / c = c - b
c += a
print("Add c value by a =" , c)
c -= b
print("Subtract c value by b =" , c)

# multiply c = c * a 
c *= a
print("multiply c value by a =" , c)

# Divide  c = c / a 
c /= a
print("Divide c value by a = " , c)

# Mod of dividing c by a , c = c % a 
c  %= a 
print("Mod c value by a = " , c)

# Exponent or power c by a , c = c ** a 
c **= a
print("power c value by = " , c)

# floor Division or integer division c = c // a  
c //= a
print("Integer Division c value by a = " , c)

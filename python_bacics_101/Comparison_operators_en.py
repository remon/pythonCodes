# Examples on how to uses Python Comparison Operators 
'''
what is comparison Operators means?
These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.

		Operator 	| Description
	------------------------------------------
	== equal	 	| If the values of two operands are equal, then the condition becomes true. a == c that means that both variables have equal value.
	!= or <> not equal	| If values of two operands are not equal, then condition becomes true.
	> greater than	 	| If the value of left operand is greater than the value of right operand, then condition becomes true.
	< less than		| If the value of left operand is less than the value of right operand, then condition becomes true.
	>= greater or equal	| If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
	<= less or equal	| If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
	
when do we use it ? 
we use this kind of operators with condition statements or in loops conditions
''' 
from __future__ import print_function
a = 10 ; b = 10

#equal 
if a == b :
	print("a is equal to b")

#not equal 
# for this to work we will increase the value of a by 10 by using Assignment operator
a += 10
print("a=" , a)
if a != b :
	print("a is not equal to b") 

# greater than 
if a > b :
	print("a is greater than b")

# less than 
if b < a :
	print("b is less than a")
# greater or equal 
if a >= b :
	print("a is either greater or equal to b")

#less or equal
if b <= a :
	print("b is either less or equal to a")





# Examples on how to uses Python Arithmetic Operators
'''
What is the operator in Python?
Operators are special symbols in Python that carry out arithmetic or logical computation.
The value that the operator operates on is called the operand.
for example: 2 + 3 = 5 
Here, + is the operator that performs addition.
2 and 3 are the operands and 5 is the output of the operation.

what is Arithmetic Operators means ? 
	Operator 		| Description
	-----------------------------------------------
	+ Addition 		| Adds values on either side of the operator.
	- Subtraction 		| Subtracts right hand operand from left hand operand.
	* Multiplication 	| Multiplies values on either side of the operator 
	/ Division 		| Divides left hand operand by right hand operand 
	% Modulus 		| Divides left hand operand by right hand operand and returns remainder
	** Exponent		| Performs exponential (power) calculation on operators
	// Floor Division	| he division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero

when do we use it ? 
we use this kind of every where form basic math operation to loops or condition statements 
''' 
from __future__ import print_function
a = 20 ; b = 10

# Addition operator
c = a + b
print("Addition value =" , c)

# Subtraction operator
c = a - b
print("Subtraction value = " , c)

# Multipliction operator 
c = a * b
print("Multipliction value = " , c)

# Division operator 
c = a / b
print("Division value = " , c)

# Mod operator 
c = a % b
print("Mod value = " , c)

# Exponent or power operator
a = 2 ; b = 3 
c = a ** b
print("Exponent value = " , c)

# floor Division or integer division operator
'''
Note : 
In Python 3 the division of 5 / 2 will return 2.5 this is floating point division 
the floor Division or integer divisio will return 2 mean return only the integer value 
'''
a = 9 ; b = 4 
c = a // b 
print("Integer Division value = " , c)


num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
oper = raw_input('''
Enter Operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


if oper == '+':
    
    print(num1 + num2)

elif oper == '-':
  
    print(num1 - num2)

elif oper == '*':
    
    print(num1 * num2)

elif oper == '/':
    
    print(num1 / num2)

else:
    print('Invalid input')

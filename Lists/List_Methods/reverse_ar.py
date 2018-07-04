#added by @Azharoo
#Python 3

"""
The reverse() يعكس عناصر قائمة محددة.
The reverse() لا تأخذ أي عوامل.
The reverse() لا يعيد أي قيمة. يقوم فقط عكس العناصر وتحديث القائمة.
"""

#مثال 1 : Reverse a List

# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)



#Example 2: Reverse a List Using Slicing Operator

# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# Reversing a list	
#Syntax: reversed_list = os[start:stop:step] 
reversed_list = os[::-1]

# updated list
print('Updated List:', reversed_list)



#Example 3: Accessing Individual Elements in Reversed Order

# Operating System List
os = ['Windows', 'macOS', 'Linux']

# طباعة القائمة بشكل معكوس
for o in reversed(os):
    print(o)



# مثال 4 : (شرح الاستاذ الفاضل ريمون )

def my_f(list):
  list1 = list.reverse() 
  return list1

list =[10,20,40]

print(my_f(list)) ## الناتج هنا None 



def my_f(list):
  list1 = list.reverse() 
  return list

list =[10,20,40]

print(my_f(list))## [40, 20, 10]

"""
لماذا الناتجين مختلفين

ببساطة

فى المرة الاولى

reverse()
هى قامت بالتعديل على القائمة لكن لاتقوم باخراج القائمة الجديدة
 
لكن تم التعديل بالفعل على القائمة واذا تمت طباعة القائمة نجد ان
 
قيم العناصر قد انقلبت بالعكس

وهو ماحدث فى الكود الحالى عندما قمنا بارجاع قيمة القائمة

وتمت طباعة القيمة بالفعل

بينما فى المرة الاولى … ما طلبنا اخراجه هو العملية نفسها … وليست القيمة
"""

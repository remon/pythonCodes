#added by @Azharoo
#Python 3

"""
The reverse() íÚßÓ ÚäÇÕÑ ŞÇÆãÉ ãÍÏÏÉ.
The reverse() áÇ ÊÃÎĞ Ãí ÚæÇãá.
The reverse() áÇ íÚíÏ Ãí ŞíãÉ. íŞæã İŞØ ÚßÓ ÇáÚäÇÕÑ æÊÍÏíË ÇáŞÇÆãÉ.
"""

#ãËÇá 1 : Reverse a List

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

# ØÈÇÚÉ ÇáŞÇÆãÉ ÈÔßá ãÚßæÓ
for o in reversed(os):
    print(o)



# ãËÇá 4 : (ÔÑÍ ÇáÇÓÊÇĞ ÇáİÇÖá Ñíãæä )

def my_f(list):
  list1 = list.reverse() 
  return list1

list =[10,20,40]

print(my_f(list)) ## ÇáäÇÊÌ åäÇ None 



def my_f(list):
  list1 = list.reverse() 
  return list

list =[10,20,40]

print(my_f(list))## [40, 20, 10]

"""
áãÇĞÇ ÇáäÇÊÌíä ãÎÊáİíä

ÈÈÓÇØÉ

İì ÇáãÑÉ ÇáÇæáì

reverse()
åì ŞÇãÊ ÈÇáÊÚÏíá Úáì ÇáŞÇÆãÉ áßä áÇÊŞæã ÈÇÎÑÇÌ ÇáŞÇÆãÉ ÇáÌÏíÏÉ
 
áßä Êã ÇáÊÚÏíá ÈÇáİÚá Úáì ÇáŞÇÆãÉ æÇĞÇ ÊãÊ ØÈÇÚÉ ÇáŞÇÆãÉ äÌÏ Çä
 
Şíã ÇáÚäÇÕÑ ŞÏ ÇäŞáÈÊ ÈÇáÚßÓ

æåæ ãÇÍÏË İì ÇáßæÏ ÇáÍÇáì ÚäÏãÇ ŞãäÇ ÈÇÑÌÇÚ ŞíãÉ ÇáŞÇÆãÉ

æÊãÊ ØÈÇÚÉ ÇáŞíãÉ ÈÇáİÚá

ÈíäãÇ İì ÇáãÑÉ ÇáÇæáì … ãÇ ØáÈäÇ ÇÎÑÇÌå åæ ÇáÚãáíÉ äİÓåÇ … æáíÓÊ ÇáŞíãÉ
"""

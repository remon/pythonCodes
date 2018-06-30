from __future__ import print_function 
# هذا الملف يحتوي على بعض الامثله عن السلاسل النصيه للغة البايثون
#ماهي السلاسل النصية في البايثون ؟ 
# السلاسل النصيه هي النوع الاكثر شعبية في لغة البايثون
#  نستطيع ان ننشئها بسهوله بواسطة علامات الاقتباس  
#  لغة البايثون تتعامل مع علامات الاقتباس الفردية والزوجية على حد سواء 
# يمكن إنشاء السلاسل النصية بسهوله كإسناد قيمة إلى متغير 
# مصدر التعريف  https://www.tutorialspoint.com/python/python_strings.htm


#مثال 1
#تمت مشاركتة بواسطة  @remon
# يقوم هذا المثال بطباعة السلسلة النصيه Hello World 
str1 ="Hello World"
print(str1) # --> Hello World


#مثال 2
#تمت مشاركتة بواسطة  @remon
# يقوم هذا المثال بتوضيح تعامل الارقام كسلاسل نصية بداخل علامتي الاقتباس
str2 ='Hello World 2'
print(str2) # --> Hello World 2

#مثال 3
#تمت مشاركتة بواسطة  @remon
# مثال آخر عن طريقة تخزين الارقام كسلاسل نصية
str3 ="2018"
print(str3) # --> 2018 

#مثال 4
#تمت مشاركتة بواسطة  @tony.dx.3379aems5
# يوضح هذا المثال طريقة ..... 
str4 = "Hello 2 My friends 3"
num1 = int(str4[str4.find("2")])
num2 = int(str4[-1])
result = num1 + num2 
print(result)


#مثال 5
#تمت مشاركتة بواسطة  @Takeo. yassine messaoudi 
# يوضح هذا المثال طريقة إستخدام الدالة 
# replace(old,new)
# لإستبدال الحروف في السلسلة النصية 
str1 = "1 million arab coders "
a = str1.replace("m" , "M")
print (a) # --> 1 Million arab coders

#مثال 6
#تمت مشاركتة بواسطة  @ammore5
# يوضح هذا المثال طريقة جمع سلسلتين نصيتين وطباعتهما  

str1 = "hi "
str2 = "there !"
print (str1 + str2) # --> hi there !
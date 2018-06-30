#added by Yassine Messaoudi AKA = TaKeO90 
#This class is about to print kids info 
#Also use inheritance example 

class Kid_info:



    def __init__(self, first_name, last_name, age,school_level ) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school_level = school_level 

#Example 
kid = Kid_info("Ahmed", "issa","10","primary school")


print (kid.first_name)
print (kid.last_name)
print (kid.age)
print (kid.school_level)


#inheritance example 

class Parent(Kid_info) :



    def __init__(self, first_name, last_name , age, work, number_of_kids):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.work = work
        self.number_of_kids = number_of_kids


Father = Parent("ahmed", "jalal", "35", "engenieer" , "2")

print (Father.work)
                

    


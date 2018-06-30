from __future__ import print_function
#declare a class

#Synatx
  #class ClassName:
  #block of code

#Example 1
# __init__  passing initial values to your object

class Car:
    
    'Print Car Name And Price'

    def __init__(self,CarName,Price):
           self.CarName = CarName
           self.Price = Price
       
NewCar = Car("I8", 200000)

print("Car Name " + NewCar.CarName + "  Car Price " + str(NewCar.Price))


print("Car.__doc__:", Car.__doc__)



             
                
    
        
        

 

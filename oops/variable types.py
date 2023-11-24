class Phone():
   def __init__(self,brand,price,chargerType):
     #chargerType="C-type"                              #class variable is used for common type of declaration
     self.brand= brand
     self.price= price                                  #here self is called instance variable when ever the new object creates the self variable initialize the value through  constructor and work as an instant variable 
     self.chargerType= chargerType
   def display(self):
     print("Brand : ",self.brand)
     print("Price : ",self.price)
     print("chargerType : ",self.chargerType)

p1=Phone("Redmi",23456,"C-type")
p1.display()
p2=Phone("google",234567,"B-type")
p2.display()




class Laptop():
   def __init__(self):
     self.brand =""
     self.price=78894
   def setPrice(self,price):                     #in what are all  method we using self then it is called instance method 
     self.price=price
   def getPrice(self):
     print(self.price)
hp=Laptop()
hp.getPrice()
hp.setPrice(466544)
hp.getPrice()

#create a class called Student.
#create a variable name and register number.
#create a function called diplay which should display the name and register num of the student.


class Student():
    def __inti__(self):
        self.name-""
        self.regNo=0
    def display(self):
        print("Name: ",self.name)
        print("Reg No: ",self.regNo)
s1= Student()
s1.name="yogesh"
s1.regNo=36
s2= Student()
s2.name="Rohit sharma"
s2.regNo=45

s1.display()
s2.display()

#create a class called Fruits
#create a variable called color using __init__ method.
#create a object called apple "pass the color variable as a parameter through object"

class Fruits:
  def __init__(self,col):
    self.color=col
  def display(self):
    print(self.color)

apple=Fruits("red")
apple.display()

#create a class called Teacher
#create a variable name and register number using constructor.
#create a function called dsiplay which should display the name and register number of teacher.
class Teacher():
    def __init__(self,name,regNo):
        self.name=name
        self.regNo=regNo
    def display(self):
        print("Name : ",self.name)
        print("Regsiter number : ",self.regNo)

t1 = Teacher("shalini",56)
t2= Teacher("rohini",57)
t1.display()
t2.display()

#create a class called calculator
#create a 2 variable a and b
#create a function called add, sub, mul, div, should take two variables as a parameter.
#pass thr a and b valur through object()
class Calculator():
    def add(self,a,b):
        print(a+b)
    def sub(selfa,b):
        print(a+b)
    def mul(self,a,b):
        print(a+b)
    def div(self,a,b):
        print(a+b)
num1= Calculator()
num2= Calculator()
a=int(input("A:"))
b=int(input("B:"))
num1.add(a,b)
      
    







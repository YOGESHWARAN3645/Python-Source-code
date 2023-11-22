#Functions

#syntax

def welcome():
    print("Welcome to functions")

welcome()



#No Return type without argument

def add():
    a=int(input("A:"))
    b=int(input("B:"))
    c= a+b
    print("Total:",c)

add()


#No return type with argument

def sub(a,b):
    c=a-b
    print(c)

sub(23,54)


#Return type without argument

def mul():
    a=int(input("A:"))
    b=int(input("B:"))
    c=a*b

    return c

x=mul()
print("Total:",x)

#Return type with argument

def div(a,b):
    c=a/b
    return c

x=div(23,4)
print("Divide:",x)
    

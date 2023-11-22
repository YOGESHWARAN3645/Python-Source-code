#Function arguments

#Default argument
#defining a function
def default(n1=20,n2=40):
    print("N1:",n1)
    print("N2:",n2)

# calling a function with one arg
print("passing one arg")
default(10)


#calling a function with two arg
print("passing two arg")
default(10,30)



#Keyword arguments
#defining a function
def keyword(n1,n2):
    print("N1:",n1)
    print("N2:",n2)

#Passing without Keyword

print("Passing without Keyword")
keyword(23,45)


#Passing with Keyword

print("Passing withKeyword")
keyword(n2=23,n1=45)


#Required arguments
#defining a function
def required(n1,n2):
    print("N1:",n1)
    print("N2:",n2)

# calling a function with one arg

try:
    required(10)
except:
    print("passing only one  arg")
    


#calling a function with two arg
print("passing two arg")
required(10,30)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                










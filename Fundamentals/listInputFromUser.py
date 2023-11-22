#list 
# the list is nothing it is like an array 


emp1=[]                                # typr of a emp is list type
print(type(emp1))

emp2=[9231,9228,9222]
print(emp2[0])


emp3=[9231,9228,9222]                 #to join the each index 
print(emp3)

emp4=[]
print("Enter the emp")
 
while True:                            #loop for getting list input from the user
 id=input()
 if id:
  emp4.append(id)
 else:
  break

print('\n'.join(emp4))






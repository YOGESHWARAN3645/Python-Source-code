#elif

num1,num2,num3=int(input("enter 3 num").split())

if num1>num2:
 max=num1
elif num2>num1:
 max=num2
elif num3>max:
 max=num3
print("Ans=",max)

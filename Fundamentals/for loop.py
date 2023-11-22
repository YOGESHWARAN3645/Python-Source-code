#for loop
name="yogesh";
for i in name:
    print(i,end="")
print("")                    #STRING TYPE
j=1
for j in name:
    print(j,end="")

print("")   
n=1                         #Integer Type
for n in range(10):
    print(n,end="")


print("")
for m  in range(20):
    if(m!=20):               #for else
      print(m,end="")
else:
    print("Finished")
print("")

l=int(input("L:"))
k=0
for k in range(l):           #nested for
      for m in range(k):
        print("x",end="")
      print("")
    
else:
    print("yogi")

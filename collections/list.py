#list
#sequence type #mutable type
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print(a[1])
print(a[-1])
print(a[0:-4])
print(a[2:4])
print(a[:5])
print(a[-1:-5])
print("___________________________")

a=[9231,"yogesh",7.83,True,]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print("___________________________")

a.clear()
print(a)
a=[2,1,5,6,2,4,5,6,3,2,14,7,8,9,5,8,6,7,9]
b=a.copy()
print(b)
print(a.count(5))
print(a.index(14))
print(len(a))
print(max(a))
print(min(a))
a.pop(2)
print(a)
a.remove(4)
print(a)
a.append("yogi")
print(a)
b=["hari,sandy"]
a.extend(b)
print(a)
a.insert(2,"hitman")
print(a)
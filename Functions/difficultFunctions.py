#variable Length arguments

def test(g):
    n1=input();                 
    return n1

a=23
rv=test(a)
print("int:",rv)


a="yogi"
rv=test(a)
print("string:",rv)

a=False
rv=test(a)
print("bool:",rv)

def test1(*args_list):
    n1=[]
    for i in args_list:
        n1.append(i.upper())
    return n1

b=['yogo','45435','45.5']
m=test(b)
print(m)



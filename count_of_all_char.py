a=input("enter the string :")
l=[]
b=list(dict.fromkeys(a))
for _ in range(len(b)):
    l.append(a.count(b[_]))
print("char      count ")
for _ in range(len(b)):
    print(b[_],"        ",l[_])

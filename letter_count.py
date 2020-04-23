s=input("Enter the string ")
s1=list(set(s))
for item in s1:
    print(item," :  ",s.count(item))

a=input("enter the string : ")
a=a.split(" ")
s=0
i=" " 
for item in a:
    if len(item)>s:
        s=len(item)
        i=item
print("the string with max length is ",i)

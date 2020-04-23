s=input("Enter the string ")
s=s.split(" ")
length=0
word=""
for item in s:
    if length<len(item):
        length=len(item)
        word=item
print("Word with largest length  : ",word," is :",length)
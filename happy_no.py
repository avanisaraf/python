def happyno(n):
    n=list(n)
    n=list(map(int,n))
    n=list(map(lambda a:a*a,n))
    return sum(n)


n=input("Enter the no.")
r=n
while(int(r)!=1 and int(r)!=4):
    r=happyno(str(r))
if r==1:
    print(n," : is a happy no")
else:
    print(n," : is not a happy no")
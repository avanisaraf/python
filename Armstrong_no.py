#*********************WAP for Armstrong no.********************
import math
n=input("\nEnter the no's ")
n1=list(n)
n1=list(map(lambda a:int(a),n1))
n1=list(map(lambda a:a*a*a,n1))
if int(n)==sum(n1):
    print(n,"Is a Armstrong no.")
else:
    print(n,"Is not a Armstrong no.")
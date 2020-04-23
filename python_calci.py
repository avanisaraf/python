def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    x=int(input("Enter the  1st no."))
    y=int(input("Enter the  2nd no."))
    a=input("Enter the operand")
    if a=="+":
        print(f"sum of {x} and {y} is :",sum(x,y))
    elif a=="*":
        print(f"multiplication of {x} and {y} is :",mul(x,y))
    elif a=="-":
        print(f"subtraction of {x} and {y} is :",sub(x,y))
    elif a=="/":
        print(f"division of {x} and {y} is :",div(x,y))
    else:
        break

    
    

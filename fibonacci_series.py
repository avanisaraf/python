#WAP for printing Fibonacci series
n = int(input("\nEnter the no. of Element"))
if n == 0:
    print("Incorrect value")
elif n == 1:
    print(0)
elif n == 2:
    print(0,1)
else:
    f1 = 0
    f2 = 1
    print(f1,f2,end=" ")
    for n in range(n):
        s = f1 + f2
        print(s,end=" ")
        f1 = f2
        f2 = s
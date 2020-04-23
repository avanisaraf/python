#*********************WAP for Leap Year*****************
year = int(input("Enter Year: "))
if (year%4==0 & year%100!=0) | year%4==0:
    print(year,"Is a leap year")
else:
    print(year,"Is not a leap year")
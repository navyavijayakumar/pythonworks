yr=int(input("enter year:"))

if (yr%4==0 and yr%100!=0) or (yr%400==0 and yr%100==0):
    
    print(f"{yr} is leap year")

else:

    print(f"{yr} is not leap year")

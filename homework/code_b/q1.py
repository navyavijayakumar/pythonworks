num1=int(input("enter a number:"))

num2=int(input("enter second number:"))

num3=int(input("enter third number:"))


if num1>num2 and num1>num3:

    if num2>num3:
        print(f"{num2} is secondlargest")
    else:
        print(f"{num3} is secondlargest")


elif num2>num1 and num2>num3:

    if num1>num3:
         print(f"{num1} is secondlargest")
    else:
         print(f"{num3} is secondlargest")     

  
elif num3>num1 and num3>num2:
    
    if num1>num2:
         print(f"{num1} is secondlargest")
    else:
         print(f"{num2} is secondlargest")
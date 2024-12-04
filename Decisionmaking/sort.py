
num1=int(input("enter  first number:"))

num2=int(input("enter  second number:"))

num3=int(input("enter  third number:"))

print(f"numbers before sorting {num1},{num2},{num3}")

if num1>num2 and num1>num3:


    if num2>num3:

        print("after sorting",num1,num2,num3)

    else:    

        print("after sorting",num1,num3,num2)


elif num2>num1 and num2>num3:
    

    if num1>num3:
    
        print("after sorting",num2,num1,num3)

    else:     
        
        print("after sorting ",num2,num3,num1,)


elif num3>num1 and num3>num2:
    

    if num1>num2:
         
         print("after sorting",num3,num1,num2)

    else:

        print("after sorting",num3,num2,num1)    
   
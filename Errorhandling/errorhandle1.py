num1=int(input("enter num"))
num2=int(input("enter num"))

try:

    result=num1/num2
    print(result)
    
except:

    num2=int(input("enter num"))
    result=num1/num2
    print(result)

finally:

    print("File Write")
    print("database commit")




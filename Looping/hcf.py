
num1=int(input("enter a number:"))
num2=int(input("enter another number:"))
hcf=1

# min_num=num1 if num1<num2 else num2

min_num=min(num1,num2)

for i in range(1,min_num+1):

    if num1%i==0 and num2%i==0:
        print(i)
        hcf=i
print("hcf=",hcf)        
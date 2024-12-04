
num1=int(input("enter a number:"))
num2=int(input("enter another number:"))

max_num=max(num1,num2)

for i in range(max_num,(num1*num2)+1,max_num):
    
    if i%num1==0 and i%num2==0:
        print(i)
        break       

# min_num=min(num1,num2)

# for i in range(1,min_num+1):

#     if num1%i==0 and num2%i==0:
#         hcf=i

# print("hcf=",hcf)         

# product=num1*num2
# lcm=product/hcf
# print("lcm=",lcm)
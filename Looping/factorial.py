
# i=1
# n=int(input("enter a number:"))
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)   

num=int(input("enter a number:"))
fact=1
for n in range(1,num+1):
    fact=fact*n
print(fact)   

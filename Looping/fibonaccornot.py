
# num=int(input("enter a number:"))
# prev=0
# curr=1
# next=0
# is_fibo=False
# for i in range(1,num+1):

#     next=prev+curr
#     prev=curr
#     curr=next

#     if  next==num:
#         is_fibo=True
#         break
# print(is_fibo)
num=int(input("enter a number:"))
prev=0
curr=1
next=0
# is_fibo=False
while(num<=next):

    next=prev+curr
    prev=curr
    curr=next
    print(next)

#     if  next==num:
#         is_fibo=True
#         break
# print(is_fibo)
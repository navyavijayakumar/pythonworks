#LIST
# colour=["red","green"]
# colour[0]="blue"
# print(colour)

# expenses=[12000,13000,14000,11000,12000]
# expenses[0]=15000
# print(expenses)

# expenses=[12000,13000,14000,11000,12000]
# for exp in expenses:
#     print(exp)

# expenses=[12000,13000,14000,11000,12000]
# total=0
# for exp in expenses:
#     total+=exp
# print(total)   

# expenses=[10000,12000,12000,12000,12000,10000]
# min_exp=expenses[0]
# for exp in expenses:
#     if exp <min_exp:
#         min_exp=exp
# print(min_exp)        

# max_exp=expenses[0]
# for exp in expenses:
#     if exp>max_exp:
#         max_exp=exp
# print(max_exp)        

# avg=0
# sum=0
# length=len(expenses)
# for exp in expenses:
#         sum+=exp
#         avg=sum/length
# print(avg)    

expenses=[12000,10000,12000,12000,12000,12000,10000]
frequent_expense=expenses[0]

for exp in expenses:
    max_count=0
    count=0
    for i in expenses:
        if i==exp:
            count+=1
    if count > max_count:
            max_count = count
            frequent_expense = exp
print(frequent_expense)

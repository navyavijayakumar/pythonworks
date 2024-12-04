
# def factorial(num):
#     fact=1
#     while(num!=0):
#       fact=num*fact
#       num=num-1
#     print(fact)
# factorial(3)      
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
result=factorial(3)
print(result)
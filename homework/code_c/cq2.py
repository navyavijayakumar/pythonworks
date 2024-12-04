num=int(input("enter number:"))
is_prime=True
if num==1:
    is_prime=False 
for i in range(2,num):
    if num%i==0:
        is_prime=True
        
print("prime" if is_prime==True else "not prime")            

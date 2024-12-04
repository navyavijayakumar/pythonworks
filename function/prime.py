def prime(num):

    is_prime=True
    if num==1:
        is_prime=False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    print(is_prime)        
prime(1)    
 
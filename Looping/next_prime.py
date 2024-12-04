def next_prime(num):
    num+=1
    for i in range(2,num):
        if num%i==0:
            num+=1
    return num
print(next_prime(7))

def perfect_number(num):
    total=0
    for i in range(1,num):
        if num%i==0: 
            total=total+i
    return "perfect" if total==num else "not perfect"

print(perfect_number(11))


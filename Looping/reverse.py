
i=0

num=int(input("enter number:"))

print(f"number before reversing {num}")

while(num>0):
    dig=num%10
    i=i*10+dig
    num=num//10
    
print(f"reversed number={i}")   
    


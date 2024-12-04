num=int(input("enter a number:"))
i=0
org=num

while(num>0):
     dig=num%10
     i=i*10+dig
     num=num//10
     
result="palindrome" if org==i else "not palindrome"
print(result) 

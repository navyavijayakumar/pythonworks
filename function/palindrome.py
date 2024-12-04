def palindrome(num):
    org=num
    i=0
    while(num>0):
        dig=num%10
        i=i*10+dig
        num=num//10
    
    return "palindrome" if org==i else "not palindrome"
print(palindrome(541))
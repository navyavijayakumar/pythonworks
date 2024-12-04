
def armstrong(num):
    count=len(str(num))
    org=num
    sum=0
    while(num!=0):
        dig=num%10
        exponent=dig**count
        sum=sum+exponent
        num=num//10    
    return "armstrong" if org==sum else "not armstrong"
print(armstrong(1634))


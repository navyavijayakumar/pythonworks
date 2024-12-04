
num=int(input("enter a number:"))
count=len(str(num)) 
orginal=num
sum=0
while(num!=0):
    dig=num%10
    exponent=dig**count
    sum=sum+exponent
    num=num//10  
print(sum)
result=("armstrong" if orginal==sum else "notarmstrong")
print(result)


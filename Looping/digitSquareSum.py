
num=int(input("enter a number:"))
sum=0
square=0

while(num !=0):

    dig=num%10
    square=dig*dig #OR square=dig**2
    sum=sum+square
    num=num//10

print("digit square sum=",sum)

num = int(input("Enter a number:"))
lar_dig=0
while (num > 0):
    dig = num % 10  

    if dig>lar_dig:
        lar_dig=dig       
    num = num // 10 

print(lar_dig,"is largest")    





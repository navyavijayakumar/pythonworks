num=int(input("enter num:"))
dic={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
    20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
digits=[]
while(num!=0):
    dig=num%10
    digits.append(dig)
    num=num//10
digits=digits[::-1]
# result=[v for k,v in dic.items() if k==dig]
# num=num//10
# print(result)
for n in digits:
    for k,v in dic.items():
        if k==n:
            print(v,end=" ")



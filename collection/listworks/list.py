lst=[2,3,4,5]
total=0
for i in range(0,len(lst)):
    total=total+lst[i]
for j in range(0,len(lst)):
    sum1=total-lst[j]    
    print(sum1,end=" ")
    
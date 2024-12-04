
lst=[1,1,2,2,5,3,3,4,4]
lst.sort()
duplicate_number=[]
non_duplicate_number=[]
for i in range(0,len(lst)-1):
    j=i+1
    result=lst[j]-lst[i]
    if result==0:
        if lst[i] not in duplicate_number:
          duplicate_number.append(lst[i])
          
for num in lst:      
   if num not in duplicate_number:
      non_duplicate_number.append(num)
result=duplicate_number+non_duplicate_number      
result.sort(reverse=True)
print(result)
print(result[1])
 
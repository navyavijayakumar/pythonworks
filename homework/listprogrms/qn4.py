 
lst1=[1,2,2,3,3,4,3]
lst1.sort()
lst2=[]
for i in lst1:
    if i not in lst2:
        count=lst1.count(i)
        print(f"{i}={count}")
        lst2.append(i)



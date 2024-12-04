lst1=["apple","mango","onion","potato"]
lst2=[100,200]
result={}
for i in range(0,len(lst2)):
    list_one_index_element=lst1[i]
    list_two_index_element=lst2[i]
    result[list_one_index_element]=list_two_index_element
    
bal_lst=lst1[len(lst2):]
for index,element in enumerate(bal_lst):
    result[element]=index+1
print(result)    
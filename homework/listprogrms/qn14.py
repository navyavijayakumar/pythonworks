lst=[1,2,3,5]
old_element=int(input("enter element:"))
new_element=int(input("enter new element:"))
if old_element in lst:
    index =lst.index(old_element)  
    lst[index] = new_element 
print(lst)
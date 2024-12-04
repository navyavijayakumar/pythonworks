arr=[1,2,3,4]
for i in range(0,len(arr)):
    index=int(input("enter index number:"))
    del_element=arr.pop(index)
    print(arr)
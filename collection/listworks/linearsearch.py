arr=[2,4,6,8,3,7]
number=int(input("enter number:"))
search_element=False

for i in range(0,len(arr)):
    if arr[i]==number:
        search_element=True
        break
print(search_element)


arr=[100,200,300,400,500,600,700,800]

# # for i in range(len(arr)):
# #    if i%2!=0:
# #         arr1.append(arr[i])
# # print(arr1)

# arr1=[arr[i] for i in range(len(arr)) if i%2!=0 ]
# for i in range(1,len(arr),2):
#     element=arr1.pop()
#     arr[i]=element
# print(arr)


# odd_position_number=[num for index,num in enumerate(arr) if index%2!=0]
# # odd_position_number.reverse()
# print(odd_position_number)
# for i in range(1,len(arr),2):
#     element=odd_position_number.pop()
#     arr[i]=element
# print(arr)

left=1
right=len(arr)-1
if right%2==0:
    right-=1
while(left<right):
    arr[left],arr[right]=arr[right],arr[left]   
    left=left+2
    right=right-2
print(arr)



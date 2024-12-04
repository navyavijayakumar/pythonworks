# arr=[2,3,4,5]
# sum=7
# arr1=arr[0]
# for i in range(0,len(arr)-1):
    
#         for j in range(i+1,len(arr)):
#             curr_sum=arr[i]+arr[j]
#             if sum==curr_sum:
#                   print(arr[i],arr[j])
#                   break

arr=[1,2,3,4,5,6]  
sum=int(input("enter a number:"))
left=0
right=len(arr)-1
while(left<right):
    curr_sum=arr[left]+arr[right]
    if sum==curr_sum:
        print(arr[left],arr[right])
        break
    elif curr_sum>sum:
        right=right-1
    elif curr_sum<sum:
        left=left+1   
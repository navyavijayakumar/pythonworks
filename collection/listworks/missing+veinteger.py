# def missing_integer(arr):
#     missing_int=arr[0]
#     for i in arr:
#         if i==missing_int:
#             missing_int=missing_int+1
#     return missing_int
# arr=[1,2,4,5]
# print(missing_integer(arr))


# def missing_integer(arr):
#     missing_int=1
#     for i in arr:
#         if i==missing_int:
#             missing_int=missing_int+1
#     return missing_int
# arr=[1,2,3,5]
# print(missing_integer(arr))


# def missing_integer(arr):
#     missing_int=1
#     for i in arr:
#         if i==missing_int:
#             missing_int=missing_int+1
#     return missing_int
# arr=[1,2,3,4,5]
# print(missing_integer(arr))

            #OR

arr=[1,2,3,4,5]
n=arr[0]
for i in range(len(arr)+1):
    if n not in arr:
        print(n)
        break
    n=n+1


# arr=[1,3,4,5]
# n=arr[0]
# for i in range(len(arr)+1):
#     if n not in arr:
#         print(n)
#         break
#     n=n+1


# arr=[1,2,3,5]
# n=arr[0]
# for i in range(len(arr)+1):
#     if n not in arr:
#         print(n)
#         break
#     n=n+1
          
             #OR

# arr=[1,6,2,5]
# i=0
# j=1
# arr.sort()
# while(i<len(arr)-1 and j<len(arr)):
#     sub=arr[j]-arr[i]
#     if sub!=1:
#         print(arr[i]+1)
#         break
#     i=i+1
#     j=j+1

         #OR

# arr=[1,6,2,5]
# i=0
# j=1
# arr.sort()
# for i in range(0,len(arr)-1):
#     j=i+1
#     result=arr[j]-arr[i]
#     if result!=1:
#         print(arr[i]+1,"is missing")
#         break


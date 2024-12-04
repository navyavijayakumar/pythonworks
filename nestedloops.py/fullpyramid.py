# rows=5
# sp=rows
# for space in range(1,rows+1):
#     sp=sp-1
#     print(end=" "*sp)
#     for row in range(space,space+1):
#         for col in range(1,row+1):
#             print("*",end=" ")    
#     print()    
# print()    

for row in range(1,7):

    for sp in range(1,7-row):
        print("",end=" ")
    for col in range(1,row+1):
        print("* ",end="")    
    print()    
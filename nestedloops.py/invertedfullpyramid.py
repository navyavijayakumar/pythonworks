
for row in range(6,0,-1):
    for sp in range(1,6-row+1):
        print("",end=" ")
    for col in range(1,row+1):
        print("* ",end="")    
    print()    
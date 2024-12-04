
for row in range(1,8):
    
    prev=0
    curr=1
    print(prev,end="\t")
    if row>1:
        print(curr,end="\t")
    
    for col in range(2,row):

        next=prev+curr
        print(next,end="\t")
        prev=curr
        curr=next

    print() 


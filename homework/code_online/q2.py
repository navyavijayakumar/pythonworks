def next_fibonacci_number(number:int):
    prev=0
    curr=1
    next=0
    is_fibo=False
    for i in range(1,number+1):
        next=prev+curr
        prev=curr
        curr=next
        if next>number:
            is_fibo=True
            break
    print(next)
next_fibonacci_number(5)            

    
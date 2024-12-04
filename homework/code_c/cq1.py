num=int(input("enter a number:"))
if num%15==0:
    print("PINGPONG")
elif num%3==0:
    print("PING")
elif num%5==0:
    print("PONG")
elif num%3!=0 or num%5!=0:
    print(num)
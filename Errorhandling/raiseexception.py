# def vote(age):
#     if age<=18:
#         raise Exception("invalid age")
#     else:
#         print("voted")
# try:
#     vote(17)
# except Exception as e:
#     print(e)


def review(rating):
    if rating<0:
        raise Exception("too low")
    elif rating>10: 
        raise Exception("too high")
    else:
        print("done")

try:
    review(11)
except Exception as e:
    print(e)            

print("hello")
print("hai")


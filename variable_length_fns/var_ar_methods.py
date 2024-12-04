# def add_numbers(*args):# accept any number of arguments as tuple

#     print(sum(args))

# add_numbers(10,20)
# add_numbers(10,20,30)

def product(*args):
    result=1
    for num in args:
        result=result*num
    return result
print(product(1,2))
print(product(10,2,4))
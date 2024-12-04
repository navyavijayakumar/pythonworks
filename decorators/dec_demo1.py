def swap_decorator(fn):

    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    
    return wrapper

def round_dec(fn):

    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        return fn(n1,n2) 
    
    return wrapper

@round_dec
@swap_decorator
def add_number(num1,num2):
    return num1+num2

@round_dec
@swap_decorator
def subtraction(num1,num2):
    return num1-num2

@round_dec
@swap_decorator
def division(num1,num2):
    return num1//num2

print(division(2.12,10))
print(subtraction(2.12,10))

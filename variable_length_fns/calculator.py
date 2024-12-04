def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":
        print(sum(args))

    if kwargs.get("operation")=="*":
        result=1
        for num in args:
            result=result*num
        print(result)
        
calculator(10,20,30,operation="+")
calculator(1,2,3,operation="*")

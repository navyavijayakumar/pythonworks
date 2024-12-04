def student_info(*args,**kwargs):
       if kwargs.get("operation")=="avg":
              total=sum(args)
              length=len(args)
              avg=total//length
              print(avg)

       if kwargs.get("operation")=="total":
              print(sum(args))
              
student_info(45,43,44,operation="avg")
student_info(45,43,44,operation="total")

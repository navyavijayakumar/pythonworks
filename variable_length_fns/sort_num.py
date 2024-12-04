def sort_num(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        print(sorted(args,reverse=True))

    if kwargs.get("reverse")=="False":
        print(sorted(args))

sort_num(1,2,3,4,5,11,reverse="True")
sort_num(1,2,3,4,5,11,reverse="False")

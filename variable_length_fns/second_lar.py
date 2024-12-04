def max_num(*args):
    sort_lst=sorted(args,reverse=True)[1]
    return sort_lst
print(max_num(10,23,78))
print(max_num(10,23,78,100,35))


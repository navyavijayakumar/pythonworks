from re import finditer
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\Regularexpression_fileworks\\socialpost.txt")
for line in f:
    post=line.rstrip("\n")

    #pattern=r"(#)+[a-zA-Z0-9]*"
    pattern=r"#\w+"
    match=finditer(pattern,post)
    for obj in match:
        print(obj.group())
from re import fullmatch

f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\Regularexpression_fileworks\\phn_numbers.txt")
for line in f:
    phone=line.rstrip("\n")
    pattern="(91)?[0-9]{10}"
    match=fullmatch(pattern,phone)
    if match!=None:
        print(phone)
    
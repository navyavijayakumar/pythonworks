from re import fullmatch
usr_input=input("enter variable:")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
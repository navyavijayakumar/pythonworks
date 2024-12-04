from re import fullmatch
usr_input=input("enter variable:")
pattern="[p-tP-T][369][0-9a-zA-Z@]*"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
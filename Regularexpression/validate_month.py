from re import fullmatch
usr_input=input("enter month:")
pattern="(0?[1-9]|1[0-2])"
match=fullmatch(pattern,usr_input)
if match==None:
        print("invalid")
else:
        print("valid")
from re import fullmatch
usr_input=input("enter gmail:")
pattern="[a-z]+[a-z0-9]{6,63}@gmail.com"
match=fullmatch(pattern,usr_input)
if match==None:
        print("invalid")
else:
        print("valid")
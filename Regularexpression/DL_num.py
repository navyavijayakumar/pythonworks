 


from re import fullmatch
usr_input=input("enter  DL num:")
pattern="[A-Z]{2}[0-9]{2} [0-9]{4}[0-9]{7}"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")

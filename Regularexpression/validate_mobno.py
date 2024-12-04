from re import fullmatch
usr_input=input("enter mobile num:")

#patten="(91)?" #optional
#pattern="(91)+" #mandatory

pattern="(91)+[0-9]{10}"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
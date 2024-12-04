
# J8369854

from re import fullmatch
usr_input=input("enter passport num:")
pattern="[A-Z]{1}[1-9]{1}[0-9]{1}[0-9]{4}[1-9]{1}"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
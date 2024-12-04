
from re import fullmatch
usr_input=input("enter Pan num:")
pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
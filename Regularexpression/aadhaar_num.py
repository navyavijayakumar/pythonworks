
from re import fullmatch
usr_input=input("enter  Aadhaar num:")
pattern="[0-9]{4} [0-9]{4} [0-9]{4}"
match=fullmatch(pattern,usr_input)
if match==None:
    print("invalid")
else:
    print("valid")
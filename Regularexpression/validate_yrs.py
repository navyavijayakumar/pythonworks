#validate yrs from 1800-2024
from re import fullmatch
usr_input=input("enter yr:")
# pattern="(1[89]{1}[0-9]{2}|2[0](1[0-9]|2[0-4]))"
pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"
match=fullmatch(pattern,usr_input)
if match==None:
        print("invalid")
else:
        print("valid")
        
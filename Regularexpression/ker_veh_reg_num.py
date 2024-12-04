# from re import fullmatch
# usr_input=input("enter vehicle num:")
# pattern="(KL|kl)+[0-9]{2}[A-Z]{1,2}[0-9]{4}"
# match=fullmatch(pattern,usr_input)
# if match==None:
#     print("invalid")
# else:
#     print("valid")

# KL03HA1985

from re import fullmatch
usr_input = input("Enter vehicle number: ")

pattern="(KL|kl)+(0[0-9]|[1-7][0-9|8[0-6])[A-Z]{1,2}[0-9]{4}"
match = fullmatch(pattern, usr_input)

if match is None:
    print("Invalid")
else:
    print("Valid")


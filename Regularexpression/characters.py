# "\w" => Alphanumeric ==[a-zA-z0-9]
# "\d" => Digits ==[0-9]
# "\D" => exclude Digits ==[^0-9]
# "\W" => Special Characters ==[^a-zA-Z0-9]
# "\s" => Space
# "\S" => Exclude spaces

from re import finditer 

text="I have 3 cars,2 bike and 1-Cycle"
pattern=r"\w"
match=finditer(pattern,text)
for obj in match:
    print(obj.start(),obj.group())


# text="I have 3 cars,2 bike and 1-Cycle"
# pattern=r"\d"
# match=finditer(pattern,text)
# for obj in match:
#     print(obj.start(),obj.group())


# text="I have 3 cars,2 bike and 1-Cycle"
# pattern=r"\D"
# match=finditer(pattern,text)
# for obj in match:
#     print(obj.start(),obj.group())


# text="I have 3 cars,2 bike and 1-Cycle"
# pattern=r"\W"
# match=finditer(pattern,text)
# for obj in match:
#     print(obj.start(),obj.group())


# text="I have 3 cars,2 bike and 1-Cycle"
# pattern=r"\s"
# match=finditer(pattern,text)
# for obj in match:
#     print(obj.start(),obj.group())


text="I have 3 cars,2 bike and 1-Cycle"
pattern=r"\S"
match=finditer(pattern,text)
for obj in match:
    print(obj.start(),obj.group())
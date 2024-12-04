from re import finditer

text="I have 3 cars,2 bike and 1-Cycle"

# pattern="[0-9]"
# match=finditer(pattern,text)
# for m in match:
#     print(m.group())


# pattern="[a-z]"
# match=finditer(pattern,text)
# for m in match:
#     print(m.start(),":",m.group())


# pattern="[a-zA-Z]"
# match=finditer(pattern,text)
# for m in match:
#     print(m.start(),":",m.group())


pattern="[a-zA-Z0-9]"
match=finditer(pattern,text)
for m in match:
    print(m.start(),":",m.group())
    

# pattern="[^ak ]" #exclude a,k
# match=finditer(pattern,text)
# for m in match:
#     print(m.start(),":",m.group())


# pattern="[^akA-Z0-9,\- ]"
# match=finditer(pattern,text)
# for m in match:
#     print(m.start(),":",m.group())


# pattern="[^a-zA-Z0-9]"  #chk for spcl char
# match=finditer(pattern,text)
# for m in match:
#     print(m.start(),":",m.group())
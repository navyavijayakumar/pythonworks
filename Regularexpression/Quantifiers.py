from re import finditer

text="abbabbaababababaaab"

#pattern="a{2}" #aa  
#pattern="a{1,3}" #minimum 1 maximum 3


pattern="a*" #any number including 0
match=finditer(pattern,text)
for obj in match:
    print(obj.start(),obj.group())
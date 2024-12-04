text="malayalam"

length=len(text)-1


rev_str=""

for i in range(length,-1,-1):

    rev_str+=text[i]

print(rev_str)    
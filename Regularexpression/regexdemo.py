from re import finditer

text="fatcatrunsveryfasttocatchtherat"
pattern="at"
match=finditer(pattern,text)
for m in match:
    print(m.start(),m.group())

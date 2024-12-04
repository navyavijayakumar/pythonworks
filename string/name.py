text="arunkumar@gmail.com"
index=text.index("@")
print(text[:index])

org_text="hellopython"
index=org_text.index("o")
rev_text=org_text[index-1::-1]
bal_text=org_text[index:]
result=rev_text+bal_text
print(result)
text="abbacbc"
i=0
for ch in text:
    i=i+1
    if ch in text[i:]:
        break
print(ch)
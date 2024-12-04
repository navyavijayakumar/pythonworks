text="programming"
result=""
for ch in text:
    if ch not in result:
        result+=ch
print(result)
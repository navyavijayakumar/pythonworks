path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q11.txt"
f=open(path,"r")
content=f.read()
occurrence={ch.rstrip("\n"):content.count(ch)for ch in content}
print(occurrence)
f.close()
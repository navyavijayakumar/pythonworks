path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q13.txt"
f=open(path,"r")
content=f.readlines()
print(content)
f.close()
f1=open(path,"w")
for line in content:
    if line!="\n":
        print(line.rstrip("\n"))
        f1.write(line)
f1.close()
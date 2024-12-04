path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q14.txt"
f=open(path,"r")
content=f.readlines()
f.close()
old_char="this"
new_char="that"
f=open(path,"w")
for line in content:
    
    new_line=line.replace(old_char,new_char)
    f.write(new_line)
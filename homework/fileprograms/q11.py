path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q11.txt"
f=open(path,"r")
content=f.readlines()
occurence={}
for line in content:
    line=line.rstrip("\n")
    if line in occurence:
        occurence[line]+=1
    else:
        occurence[line]=1    
print(occurence)
duplicates={k for k,v in occurence.items()if v>1}
print(duplicates)
f.close() 
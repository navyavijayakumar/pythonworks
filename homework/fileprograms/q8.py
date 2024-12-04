f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q3.txt","r")
lst=[]
for line in f:
    line=line.rstrip("\n")
    line=line.split(" ")
    lst.extend(line)
cnt=lst.count("simple")
print(cnt)
f.close()
    
    
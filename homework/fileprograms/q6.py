path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q3.txt"
f=open(path,"r")
lst=[]
for line in f:
    line=line.rstrip("\n")
    line=line.split(" ")
    lst.extend(line)
long_word=max(lst,key=lambda l:len(l))
print(long_word)
f.close()
    
    
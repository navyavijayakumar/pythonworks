f1=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q3.txt","r")
for w in f1:
    words=w.split(" ")
    length=len(words)
print(words) 
print(length)   
f1.close()
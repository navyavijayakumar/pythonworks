f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\fruits.txt","r")
fruits=[]
for line in f:
    fruits.append(line.rstrip("\n"))

print(fruits)
f.close()
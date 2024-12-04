path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q4.txt"
f1=open(path,"r")
write_path="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q5.txt"
f2=open(write_path,"w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()    
    
    
path1="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\names.txt"
path2="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q5.txt"
path3="C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q6.txt"
f1=open(path1,"r")
f2=open(path2,"r")
f3=open(path3,"w")
file1=set([line.rstrip("\n")for line in f1])
file2=set([line.rstrip("\n")for line in f2])
file3= file1.union( file2)
for line in file3:
    f3.write(line + "\n") 

f1.close()
f2.close()
f3.close()


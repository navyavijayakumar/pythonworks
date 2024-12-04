f1=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q2.txt","a")
string=input("enter a string:")
f1.write(string)
f1=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q2.txt","r")
content=f1.read()
print(content)
f1.close()


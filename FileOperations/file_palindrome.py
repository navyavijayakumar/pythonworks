f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\file_read.txt")
palindrome_path=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\palindrome.txt","w")
for name in f:
    name=name.rstrip("\n")
    reversed_string=name[::-1]
    if name==reversed_string:
        print(name)
        palindrome_path.write(name+"\n")
f.close()
palindrome_path.close()



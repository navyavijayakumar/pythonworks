f1=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\q4.txt","r")
num=0
for line in f1:
    line=line.rstrip("\n")
    num=num+1
    
    if num%2==0:
        print(f"{num}:{line}")  
f1.close()
# for num,line in enumerate(f1,start=1):
#     if num%2==0:
#         print(line.rstrip("\n"))
# f1.close()        
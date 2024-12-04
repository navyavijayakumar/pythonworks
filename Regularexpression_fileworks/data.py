from re import findall 
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\Regularexpression_fileworks\\data.txt")
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
dates=findall(pattern,content)
for date in dates:
    print(date)

#05/10/2020.
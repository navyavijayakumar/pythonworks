from re import finditer,findall,fullmatch
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\Regularexpression_fileworks\\sample1.txt")

content=f.read()


pattern="https?://[\w\S./]+"

urls=findall(pattern,content)
for url in urls:
    print(url)
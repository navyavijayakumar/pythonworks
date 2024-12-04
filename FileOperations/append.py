f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\append.txt","a")
frameworks=["wordpress","springboot","odoo","fastapi"]
for fw in frameworks:
    f.write(fw+"\n")
f.close()
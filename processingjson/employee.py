from json import load
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\employee.json")
data=load(f)
for emp in data:
    print(emp)
    
f1=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\all_students.txt","r")
f2=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\failed.txt","r")
all_students=set([line.rstrip("\n")for line in f1])
failed_students=set([line.rstrip("\n")for line in f2])

# for line in f1:
#     line=line.rstrip("\n")
#     all_students.add(line)
   

# for line in f2:
#     line=line.rstrip("\n")
#     failed_students.add(line)

passed_students=all_students.difference(failed_students)

print(passed_students)
f1.close()
f2.close()




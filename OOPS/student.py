class Student:

    rno:int
    name:str
    age:int
    course:str

    def set_student(self,rno,name,age,course):
        self.rno=rno
        self.name=name
        self.age=age
        self.course=course

    def display_stu(self):
        print(self.rno,self.name,self.age,self.course)

stu_inst=Student()
stu_inst.set_student(10,"Navya",21,"Python Django")
stu_inst.display_stu()

#employee

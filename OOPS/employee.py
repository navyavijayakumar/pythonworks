class Employee:

    id:int
    name:str
    age:int
    department:str

    def set_employee(self,id,name,age,department):
        self.id=id
        self.name=name
        self.age=age
        self.department=department

    def display_emp(self):
        print(self.id,self.name,self.age,self.department)

stu_inst=Employee()
stu_inst.set_employee(10,"Navya",21,"hr")
stu_inst.display_emp()

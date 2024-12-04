#MULTIPLE

class Person:
    name:str
    age:int
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person_info(self):
        print(self.name,self.age)

class Employee:
    emp_id=int
    emp_salary:int
    
    def __init__(self,emp_id,emp_salary):
        self.emp_id=emp_id
        self.emp_salary=emp_salary

    def display_emp_info(self):
        print(self.emp_id,self.emp_salary)

class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,emp_salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,emp_salary)

        self.department=department

    def display_manager_info(self):
        self.display_person_info()
        self.display_emp_info()
        print(self.department)

manager_inst=Manager("Navya",21,99,40000,"hr")
manager_inst.display_manager_info()

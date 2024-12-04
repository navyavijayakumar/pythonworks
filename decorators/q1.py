class Person:
    name:str
    age:int

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def get_age(self):
        print(self.age)

    @property
    def get_name(self):
        print(self.name)
        
person_inst=Person("hari",20)
person_inst.get_name
        

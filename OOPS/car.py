class Car:

    name:str
    brand:str
    fuel=str
    def __init__(self,name,brand,fuel):
        self.name=name
        self.brand=brand
        self.fuel=fuel

    def display(self):
        print(self.name,self.brand,self.fuel) 

    def __str__(self): #string representation of object
        return self.name

car_inst=Car("swift","suzuki","petrol")
car_inst.display()
print(car_inst)


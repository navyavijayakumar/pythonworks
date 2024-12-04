#HIERARCHICAL

class Animal:

    name:str
    species:str

    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def __str__(self):
        return self.name

class Lion(Animal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def sound(self):
        print("Roar")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def sound(self):
        print("Meow")

lion_inst=Lion("simba","Panthera Leo")
lion_inst.sound()
print(lion_inst)

cat_inst=Cat("Marthu","Felis Catus")
cat_inst.sound()
print(cat_inst)
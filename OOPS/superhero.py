class SuperHero:

    name:str
    suit:str

    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
    def display(self):
        print(self.name,self.suit)

    def __str__(self):
        return self.name

class SpiderMan(SuperHero):

    def __init__(self, name, suit):
        super().__init__(name, suit)
    
    def superpower(self):
        print("spider sense")

class MinnalMurali(SuperHero):

    def __init__(self, name, suit):
        super().__init__(name, suit)

    def superpower(self):
        print("running")

SpiderMan_inst=SpiderMan("Spider Man","spider suit")
SpiderMan_inst.display()
print(SpiderMan_inst)


MinnalMurali_inst=MinnalMurali("Minnal murali","suit")
MinnalMurali_inst.display()
print(MinnalMurali_inst)
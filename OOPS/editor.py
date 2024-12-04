class Editor:
    
    name:str
    vendor:str

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def display(self):
        print(self.name,self.vendor)

    def __str__(self):
        return self.name

editor_inst=Editor("VScode","Microsoft")
editor_inst.display()
print(editor_inst)

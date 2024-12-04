#MULTIPLE INHERITANCE

class GrandParent:

    def m(self):
        print("Grand parent class m method")

class Parent:
    def m(self):
        print("parent class m method")

class Child(Parent,GrandParent):#causes name ambiguity error in java,in python it will inherit parent.
    def m3(self):
        print("child class m3 method")

child_inst=Child()
child_inst.m3()
child_inst.m()


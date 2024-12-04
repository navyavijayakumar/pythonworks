class GrandParent:

    def m1(self):
        print("Grand parent class m1 method")

class Parent:
    def m2(self):
        print("parent class m2 method")

class Child(Parent,GrandParent):
    def m3(self):
        print("child class m3 method")

child_inst=Child()
child_inst.m3()
child_inst.m2()
child_inst.m1()

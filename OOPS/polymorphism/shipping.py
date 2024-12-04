
class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)

class StandardShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)

ship_obj=Shipping()
exp_obj=ExpressShipping()
stand_obj=StandardShipping()

ship_obj.calculate_shipping_cost(2)
exp_obj.calculate_shipping_cost(2)
stand_obj.calculate_shipping_cost(2)
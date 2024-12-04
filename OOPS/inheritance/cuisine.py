#MULTIPLE

class Cuisine:
    cuisine_name:str

    def __init__(self,cuisine_name):
        self.cuisine_name=cuisine_name
    def display_cuisine(self):
        print(self.cuisine_name)

class MealType:
    meal_name:str
    def __init__(self,meal):
        self.meal_name=meal
    def display_meal(self):
        print(self.meal_name)

class Dish(Cuisine,MealType):
    dish:str
    def __init__(self,cuisine_name,meal,dish):

        Cuisine.__init__(self,cuisine_name)
        MealType.__init__(self,meal)
        self.dish=dish
        
    def display(self):
        self.display_cuisine()
        self.display_meal()
        print(self.dish)

            

dish_inst=Dish("italian","breakfast","pasta")
dish_inst.display()
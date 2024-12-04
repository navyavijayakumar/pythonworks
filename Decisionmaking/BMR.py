
weight=int(input("enter your weight:"))

height=int(input("enter your height:"))

age=int(input("enter age:"))

gender=input("enter gender:").lower()

print(weight,height,age,gender)

if gender=="male":

    BMR= 10*weight + 6.25*height-5*age +5

elif gender=="female":

    BMR=10*weight + 6.25*height-5*age -161

else:
    print("enter a valid gender")

print(BMR)

activity_level=int(input("""

SELECT ACTIVITY LEVEL
        press 1 for sedentary                 
        press 2 for lightly active       
        press 3 for moderatelt active
        press 4 for very active
        press 5 for extra active                                                          
"""))
if activity_level==1:
     
     Calorie_Calculation= BMR * 1.2

elif activity_level==2:

    Calorie_Calculation = BMR * 1.375

elif activity_level==3:

    Calorie_Calculation = BMR * 1.55

elif  activity_level==4:
     
     Calorie_Calculation = BMR * 1.725

elif activity_level==5:    

     Calorie_Calculation = BMR * 1.9

else:

    print("enter valid activity level")     

print(f"total number of calories you need to maintain={Calorie_Calculation}")

target_weight=int(input("enter weight to reduce in kg:"))

duration=int(input("enter duration in weeks:"))

calorie_deficit=target_weight * 7700 #7700 calories = 1kg

print(calorie_deficit)

days=duration * 7 #weeks to days

daily_calorie_deficit=calorie_deficit/days

print(f"amount of calories reduce in one day:{daily_calorie_deficit}")
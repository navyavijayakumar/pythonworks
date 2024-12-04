weight=int(input("enter weight in kg:"))
height=int(input("enter height in cm:"))
gender= input("gender:")
height_cm=height/100
BMI=(weight/(height_cm **2)) 
print(BMI)
if BMI<19:
    print("underweight")
elif BMI<25:
    print("normal weight")    
elif BMI<30:
    print("overweight") 
else:
    print("obese")
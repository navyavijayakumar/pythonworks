weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter height in cm:"))

height_in_m=height_in_cm/100

bmi=weight_in_kg/(height_in_m)**2

bmi=round(bmi)

print(bmi)

if bmi<19:

    print("underweight")

elif bmi<25:

    print("normal weight")   

elif bmi<30:

    print("overweight")   

elif bmi>=30:

    print("obese")   
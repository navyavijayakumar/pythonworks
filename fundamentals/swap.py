num1=100

num2=200

print(f"values before swapping num1={num1}, num2={num2}")

#logic1

# temp=num1

# num1=num2       

# num2=temp

#logic2

num1=num1+num2

num2=num1-num2

num1=num1-num2

print(f"values after swapping num1={num1} num2={num2}")
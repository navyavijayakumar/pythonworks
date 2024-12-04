dict1={"a":1,"b":-2,"c":-3}
# new_dict={k:abs(v) for k,v in dict1.items()}
# print(new_dict)
new_dict={k:v*-1 if v<0 else v for k,v in dict1.items()}
print(new_dict)
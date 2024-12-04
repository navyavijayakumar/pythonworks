product={"id":10,"title":"book","price":40,"brand":"classmates"}
print(product["title"])

# #update
# product["price"]=50
# print(product["price"])
# #add
# product["use_by_date"]="12-10-2030"
# print(product)
product["offer"]=5
# print(product)


#add offer as 10 if offer exist else offer as 20
if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
print(product)    


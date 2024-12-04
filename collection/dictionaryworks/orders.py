orders=["tea","coffee","coffee","porotta","tea","plainroast","plainroast","gheeroast"]
orders_dict={item:orders.count(item)for item in orders}
# orders_dict={}
# for item in orders:
#     if item in orders_dict:
#         orders_dict[item]+=1
#     else:
#         orders_dict[item]=1
print(orders_dict)            
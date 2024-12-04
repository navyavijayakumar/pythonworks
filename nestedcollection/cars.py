cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torgue"]},
]

#count
print(f"total vehicles={len(cars)}")

#print available colors of baleno
color=[c.get("colors")for c in cars if c.get("name")=="baleno"]#[0]
print(color[0])

#print all brands,(set comprehension)
brands={c.get("brand")for c in cars}
print(brands)

#print cars available in amt transmission
amt=[c.get("name")for c in cars if "amt" in c.get("transmissions")]
print(amt)

#cars available in blue color
blue_cars=[c.get("name")for c in cars if "blue"in c.get("colors")]
print(blue_cars)

#all transmission types
transmission_type=[c for car in cars for c in car.get("transmissions")]
print(set(transmission_type))

#print all colors
all_clrs={clr for c in cars for clr in c.get("colors") }
print(all_clrs)

#most popular color
clrs=[clr for car in cars for clr in car.get("colors")]
pop_clrs={clr:clrs.count(clr)for clr in clrs}
print(pop_clrs)
popular_clr=max(pop_clrs,key=lambda clr:pop_clrs.get(clr))
print(popular_clr)

#costly_car
exp=max(cars,key=lambda d:d.get("price"))
print(exp.get("name"))

#cars with min cost
min_cost=min(cars,key=lambda d:d.get("price"))
print(min_cost.get("name"))

#sorting
sort1=sorted(cars,key=lambda car:car.get("price"),reverse=True)

# srt={car.get("name"):car.get("price")for car in sort1}
# print(srt)


# srt1={car.get("name"):[car.get("price"),car.get("brand")]for car in sort1}
# print(srt1)

sorted_car={car.get("name")for car in sort1}
print(sorted_car)

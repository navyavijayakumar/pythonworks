movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

#print length of movies

print(len(movies))

#print movie titles

titles=[m.get("title")for m in movies]
print(titles)

#print movies in 2024

movie=[m.get("title")for m in movies if m.get("year")==2024]
print(movie)

#print movies if time >150
time=[m.get("title")for m in movies if m.get("run_time")>150]
print(time)

#max
print(max(movies,key=lambda m:m.get("run_time")))
#min
print(min(movies,key=lambda m:m.get("run_time")))

max_time=(max(movies,key=lambda m:m.get("run_time")))
max1=max_time.get("run_time")
m=[m.get("title")for m in movies if m.get("run_time")==max1]
print(m)

# count
movie=[m.get("title")for m in movies if m.get("year")==2024]
print(len(movie))
 
yr=[m.get("year")for m in movies]
print(yr)
yr1={y:yr.count(y)for y in yr}
print(yr1)


lan=[m.get("language")for m in movies]
lan_c={l:lan.count(l)for l in lan}
print(lan_c)
 


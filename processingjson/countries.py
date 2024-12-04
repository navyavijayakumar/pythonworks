from json import load
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\countries.json",encoding="utf-8")
data=load(f)
# print(len(data))

all_countries=[line.get("name")for line in data]
# print(all_countries)

capital=[country.get("capital") for country in data if country.get("name")=="Afghanistan"]
# print(capital[0])

#all region
all_region=[country.get("region")for country in data]
# print(set(all_region))

region_count={region:all_region.count(region) for region in all_region}
# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count)

# capital of a specific country
# user_input=input("enter a countryname:")
# capital=[country.get("capital") for country in data if country.get("name")==user_input]
# print(capital[0])


# countris with most number of borders
country_borders={country.get("name"):len(country.get("borders",[]))for country in data}
# print(country_borders)
max_country_borders=max(country_borders,key=lambda b:country_borders.get(b))
# print(max_country_borders)

# OR
max_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border)

#highst population
country_population={country.get("name"):country.get("population",[])for country in data }
max_population=max(country_population,key=lambda p:country_population.get(p))
# print(max_population)


border_share=[country.get("borders")for country in data if country.get("name")=="India" ][0]
for border in border_share:
    for country in data:
        if country.get("alpha3Code")==border:
            print(country.get("name"))

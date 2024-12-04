def display_mob_data(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("price"))
    print(kwargs.get("display"))
    print(kwargs)
display_mob_data(name="oneplus",price="32000",display="amoled")    
old_dict={"book":50,"pen":10,"toys":100,"waterbottle":200}
new_dict={k:v-(v//10) for k,v in old_dict.items()}
print(new_dict)
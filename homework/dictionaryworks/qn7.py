old_dict={"book":50,"pen":10,"toys":100,"waterbottle":200}
new_dict={k:v for k,v in old_dict.items() if v>50}
print(new_dict)
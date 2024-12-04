
text="hellopython12" 

print(text.capitalize())
cap=text.casefold()
print(cap)
# print(text.isalpha())
# print(text.isalnum())
# print(text.isdigit())
# print(text.startswith("he"))
# print(text.endswith("12"))


      #split()
# text="python java js"
# word=text.split(" ")
# print(word)


      #strip()
      #lstrip()
      #rstrip()
# text="\nthis is\n a line\n"
# word=text.strip("\n")
# print(word)


# text1="\tthis is a line\t"
# word1=text1.lstrip("\t")
# print(word1)
# word1=text1.rstrip("\t")
# print(word1)


      #replace()
# text="hello world program"
# new_text=text.replace("o","a")
# print(new_text)
# new_text=text.replace("o","a",2)
# print(new_text)

#      #slice
text="python programming"
     #index_num=012345678901234567
#      #string_object[start:end:step]
# print(text[:6])
print(text[7:])
# print(text[::2])
# print(text[::-1])
# new_text=text[::-2]
# print(new_text)

      #index()
# text="helloworld"
# print(text.index("o"))
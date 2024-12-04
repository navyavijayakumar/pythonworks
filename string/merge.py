# text1="pqrs"
# text2="abcd"
# result=""
# for i in range(len(text1)):
#     result+=text1[i]+text2[i]
# print(result)


text1="pqrst"
text2="abc"
smallest_text=text1 if text1<text2 else text2
largest_text=text1 if text1>text2 else text2
result=""
for i in range(len(smallest_text)):
    result+=text1[i]+text2[i]
balance_text=largest_text[len(smallest_text):]    
result+=balance_text
print(result)    
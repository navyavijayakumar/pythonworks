text="ABBACB"
# char_count={}
# for ch in text:
#     if ch in char_count:
#          char_count[ch]+=1
#     else:
#         char_count[ch]=1
# print(char_count)
char_count={ch:text.count(ch) for ch in text}
print(char_count)




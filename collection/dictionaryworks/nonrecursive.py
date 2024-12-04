text="ABBCAACBBCCDe"
text_dict={ch:text.count(ch) for ch in text }
print(text_dict)
text_list=[k for k,v in text_dict.items() if v==1]
print(text_list)
# for k,v in text_dict.items():
#     if v==1:
#         print(k)
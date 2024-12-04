# text="hElloworld"
# text=text.casefold()
# for ch in text:
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         print(ch)

text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
c_count=0
vowel_seq=("a","e","i","o","u")
for ch in text:
    if ch in vowel_seq:
    # if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        v_count=v_count+1

    else:
        c_count=c_count+1
print("vowel count=",v_count)
print("consonent count=",c_count)





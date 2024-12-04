# source_word="CHICKEN"
# target_word="HEN"
# is_present=True
# for char in source_word:
#     if char in target_word:
#         if source_word.count(char)==target_word.count(char) or source_word.count(char)>target_word.count(char):
#             is_present=True
#         else:
#             is_present=False
# print("kangaroo" if is_present==True else "NO")  

            #OR

# source_word="CHICKEN"
# target_word="HEN"
# source_count={c:source_word.count(c)for c in source_word}
# is_kangaroo=True
# print(source_count)
# for ch in target_word:
#       if ch in source_count.keys() and source_count[ch] > 0:
#             source_count[ch]-=1
#       else:
#             is_kangaroo=False

# print(" kangaroo" if is_kangaroo==True else"not kangaroo")            


        # OR

source_word="CHICKEN"
target_word="HENN"
character_count={}
for ch in source_word:
    if ch in character_count:
        character_count[ch]+=1
    else:
        character_count[ch]=1    
print(character_count)        
is_kangaroo=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo=False
        break
print("kangaroo word" if is_kangaroo==True else "not a kangaroo word")        







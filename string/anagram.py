# word1=input("enter first word:")
# word2=input("enter second word:")
word1="listen"
word2=" silent"
word1=word1.casefold()
word2=word2.casefold()
is_anagram=True
for ch  in word1:
    if ch not in word2:
        is_anagram=False
        break
print(is_anagram)            

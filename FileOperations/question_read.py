f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\question.txt","r")
words=[]
for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    for w in all_words:
        words.append(w)
# print(words)        

# sorted_words=sorted(words,key=lambda w:words.count(w),reverse=True)

# word_count={word:sorted_words.count(word)for word in sorted_words}
# print(word_count)
 

# most_freq=max(word_count,key=lambda w:word_count.get(w))
# print(most_freq)

word_count={w:words.count(w)for w in words}
# print(word_count)

nested_word_count=[[v,k]for k,v in word_count.items()]
# print(nested_word_count)

print(sorted(nested_word_count,reverse=True)[0]) 
f.close()
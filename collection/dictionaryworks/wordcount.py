words=["hello","hai","hello","hai","hai","hi"]
# word_count={}
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)
word_count={w:words.count(w) for w in words  }
print(word_count)
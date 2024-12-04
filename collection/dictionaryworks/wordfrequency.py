words=["hai","hello","is","this","this","hai","hai"]

word_freq={w:words.count(w) for w in words}
print(word_freq)

recursive=[k for k,v in word_freq.items() if v>1]
print(recursive)

non_recursive=[k for k,v in word_freq.items() if v==1]
print(non_recursive)

most_recursive=max(words,key=lambda word:words.count(word))
most_recursive1=max(word_freq,key=lambda word:word_freq.get(word))
print(most_recursive1)

least_recursive=min(words,key=lambda word:words.count(word))
print(least_recursive)


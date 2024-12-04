text="this is a simple programming question to find word with to maximum number of characters"
words=text.split(" ")
freq_word=max(words,key=lambda w:words.count(w))
print(freq_word)
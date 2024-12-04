sentence="this is that is this that is is"
word=sentence.split(" ")
word_freq={w:word.count(w) for w in word}
print(word_freq)
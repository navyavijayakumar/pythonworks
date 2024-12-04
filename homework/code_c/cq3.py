text = "Hello world! This is a test for finding the longest word."
words=text.split(" ")
long=max(words,key=lambda w:len(w))
print(long)


test="this is a test to remove duplicate words this test is simple"
test2="this simple test remove duplicate words"
words2=test2.split(" ")
words=test.split(" ")
words_set=set(words)
words2_set=set(words2)
print(words2_set.issubset(words_set))


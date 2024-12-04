text="this is a simple programming question to find word with maximum number of characters"
words=text.split(" ")
# def get_length(w):
#     return(len(w))
# srt_words=sorted(words,key=get_length,reverse=True)
# print(srt_words)
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)

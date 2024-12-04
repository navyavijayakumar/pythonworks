add=lambda n1,n2:n1+n2
print(add(10,20))


cube=lambda n:n**3
print(cube(3))


sub=lambda n1,n2:n1-n2
print(sub(20,10))


max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("hai","hello"))


min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("hai","hello"))

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(20,100))



words=["hello","hai","morning","test","apple"]
# def get_length(word):
#     return(len(word))
                # get_length=lambda word:len(word)
print(max(words,key=lambda word:len(word)))



text="this is a simple programming question to find word with maximum number of characters"
words=text.split(" ")
def get_length(w):
    return len(w)
print(max(words,key=get_length))

# print(max(words,key=lambda word:len(word)))


words=["hello","hai","morning","test","apple"]
srt_words=sorted(words,key=lambda word:len(word),reverse=True)
print(srt_words)


text="this is a simple programming question to find word with maximum number of characters"
words=text.split(" ")
# def get_length(w):
#     return(len(w))
# srt_words=sorted(words,key=get_length,reverse=True)
# print(srt_words)
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)

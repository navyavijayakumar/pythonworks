arr=[1,2,3,4,6]

# square=[num**2 for num in arr]
# print(square)

# result=[num+5 for num in arr]
# print(result)

# cube=[num**3 for num in arr]
# print(cube)


#             #return   #loop      #condition   
# even_numbers=[num for num in arr if num%2==0]
# print(even_numbers)

# odd_num=[num for num in arr if num%2!=0]
# print(odd_num)

# num_gt_five=[num for num in arr if num>5]
# print(num_gt_five)

# mapp=[num+1 if num>5 else num-1 for num in arr]
# print(mapp)

text=["apple","iphone",'orange',"potato"]

# words=[ch for ch in text if ch[0] in ["a","e","i","o","u"]]
# print(words)

# words=[ch for ch in text if ch[0] not in ["a","e","i","o","u"]]
# print(words)

word=max([len(ch) for ch  in text ])
longest_word=[ch for ch in text if len(ch)==word]
print(longest_word) 

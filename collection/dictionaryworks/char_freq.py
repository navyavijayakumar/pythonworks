text="ABABAAABBCD"
most_freq=max(text,key=lambda ch:text.count(ch))
print(most_freq)

print(min(text,key=lambda ch:text.count(ch)))
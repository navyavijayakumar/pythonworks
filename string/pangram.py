text="The quic brown fox jumps over the lazy dog"
# alphabets=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
alphabets="abcdefghijklmnopqrstuvwxyz"
text=text.casefold()
is_pangram=True
for ch in alphabets:
    if ch not in text:
      print(ch)
      is_pangram=False
      break 
print(is_pangram)    

text="ABABCABB"
rec={}
for ch in text:
    if ch in rec:
        if rec[ch]==1:
            print(ch)
            break
        # rec[ch]+=1
    else:
        rec[ch]=1 


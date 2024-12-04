user_input=input("enter bracket pairs:")
symbol_dict={"[":"]","{":"}","(":")","<":">"}
symbol_stack=[]
top=-1
is_valid=True

for ch in user_input:
    if ch in symbol_dict:
        top=top+1
        symbol_stack.append(ch)
    # elif top==-1:
        #   is_valid=False
    # elif ch==symbol_dict.get(symbol_stack[top])    
    #      top=top-1
    #      symbol_stack.pop()
    elif len(symbol_stack)!=0 and ch==symbol_dict.get(symbol_stack[top]):
        top=top-1
        symbol_stack.pop()
    else:
        is_valid=False

if len(symbol_stack)==0 and is_valid:
    print("valid")
else:
    print("not valid")
def smart_sub(num1,num2,reverse=False):
    #  if reverse==True:
    #       return(num2-num1)
    #  else:
        #   return(num1-num2)
    return num2-num1 if reverse==True else num1-num2
print(smart_sub(1,10,True))     
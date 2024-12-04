class Operations:#python doesn't support method overloading ,we can use *args.
    def add(self,num1,num2):
        print(num1+num2)
    
    def add(self,num1,num2,num3):
        print(num1+num2+num3)

obj=Operations()
obj.add(12,10,18)
# obj.add(10,20) #error

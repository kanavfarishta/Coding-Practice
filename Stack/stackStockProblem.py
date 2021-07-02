stock = [20,30,40,80,68,77,90,43,56]
stack = []
fData = []
maxum = -1
for i in range(0,len(stock)):
    if(stock[i]>maxum):
        maxum = stock[i]
        fData.append(i+1)
        stack  = []
        stack.append(i)
        continue
    while(True):
        if(not len(stack)):
            stack.append(i)
            fData.append(i)
            break
        if(stock[stack[-1]]>stock[i]):
            fData.append(i-stack[-1])
            break
        else:
            stack.pop()
            
            
    
print(fData)

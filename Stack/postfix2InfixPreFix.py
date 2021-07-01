stackInfix = []
stackPreFix = []
postFix = "AB+CD-*"


for i in range(0,len(postFix)):
    if(postFix[i].isalnum()):
        stackInfix.append(postFix[i])
        stackPreFix.append(postFix[i])
    else:
        a = stackPreFix.pop()
        b = stackPreFix.pop() 
        preFix = postFix[i] + b+ a
        stackPreFix.append(preFix)
        a = stackInfix.pop()
        b = stackInfix.pop()
        inFix = "(" + b + postFix[i] +  a + ")"
        stackInfix.append(inFix)
    
print(stackPreFix[0],stackInfix[0])

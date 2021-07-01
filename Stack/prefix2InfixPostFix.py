stackInfix = []
stackPostFix = []
preFix = "*-A/BC-/AKL"
inFix = ""


for i in range(len(preFix)-1,-1,-1):
    if(preFix[i].isalnum()):
        stackInfix.append(preFix[i])
        stackPostFix.append(preFix[i])
    else:
        postFix = stackPostFix.pop()+ stackPostFix.pop() + preFix[i]
        stackPostFix.append(postFix)
        
        a= stackInfix.pop()
        inFix = "(" +  + preFix[i] + stackInfix.pop()  + ")"
        stackInfix.append(inFix)
    
print(stackPostFix[0],stackInfix[0])

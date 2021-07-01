inFix = "a+b*(c^d-e)^(f+g*h)-i"
stack = []
postFix = ""
operators1 = {4:['(','{','['],3:['$','^'],2:['*','/'],'1':['+','-']}
operators = {'{':4,'[':4,'(':4,'$':3,'^':3,'*':2,'/':2,'+':1,'-':1}
closing = ['}',']',')']
def stackFunc(char,postFix):
    if(not len(stack)):
        stack.append(char)
        return postFix
    else:
        if(char in closing):
            while(True):
                if(operators[stack[-1]]==4):
                   stack.pop()
                   return postFix
                else:
                    postFix = postFix + stack.pop()
                    continue
            return postFix
        if(operators[stack[-1]] ==4):
            stack.append(char)
            return postFix
        if(operators[char]>operators[stack[-1]]):
            stack.append(char)
            return postFix
        else:
            while(True):
                if(not len(stack)):
                    stack.append(char)
                    return postFix
                if(operators[stack[-1]] == 4):
                    stack.append(char)
                    return postFix
                if(operators[char]<=operators[stack[-1]]):
                   postFix = postFix + stack.pop()
                else:
                    stack.append(char)
                    return postFix

            
for i in inFix:
    if(i.isalnum()):
        postFix = postFix+i
    else:
        postFix = stackFunc(i,postFix)
while(not len(stack)==0):
    postFix = postFix + stack.pop()
print(postFix)

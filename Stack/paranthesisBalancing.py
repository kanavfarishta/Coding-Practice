#Paranthesis Balancing
exp = "[()]{}{[()()]()}"
exp = "[()]]]]]"
stack = []
orders = {'(':')','{':'}','[':']'}
flag= False
for i in exp:
    if i in ['[','(','{']:
        stack.append(i)
    else:
        if(not len(stack)):
            flag= True
            break
        if(orders[stack.pop()] == i):
            continue
        else:
            flag= True
            break
if(flag):
    print("Incomplete Pattern")
else:
    print("Balanced")

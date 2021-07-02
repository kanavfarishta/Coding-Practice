#Next Greater Elements

numbers = [4, 5, 2, 25]
numbers = [1, 1, 2, 3, 4, 2, 1]
stack = []
fVal = []

for i in range(len(numbers)-1,-1,-1):
    if(not len(stack)):
        stack.append(numbers[i])
        fVal.append(-1)
    else:
        if(stack[-1] > numbers[i]):
            fVal.append(stack[-1])
            stack.append(numbers[i])
            continue
        while(True):
            if(not len(stack)):
                stack.append(numbers[i])
                fVal.append(-1)
                break
            if(stack[-1] > numbers[i]):
                fVal.append(stack[-1])
                stack.append(numbers[i])
                break
            else:
                stack.pop()
fVal.reverse()
print(fVal)



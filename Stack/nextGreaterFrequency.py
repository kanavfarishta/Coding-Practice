#Next Greater Frequency

freq = {}
numbers = [1, 1, 2, 3, 4, 2, 1]
numbers1 = numbers
stack = []
stack2 = []
fval2 = []
fVal = []
for i in numbers:
    try:
        freq[i] = freq[i]+ 1
    except:
        freq[i] = 1
print(freq)
for i in range(0,len(numbers)):
    numbers1[i] = freq[numbers[i]]
print(numbers1)
for i in range(len(numbers1)-1,-1,-1):
    if(not len(stack)):
        stack.append(numbers1[i])
        stack2.append(numbers[i])
        fVal.append(-1)
        fval2.append(-1)
    else:
        if(stack[-1] > numbers1[i]):
            fVal.append(stack[-1])
            fval2.append(stack2[-1])
            stack.append(numbers1[i])
            stack2.append(numbers[i])
            continue
        while(True):
            if(not len(stack)):
                stack.append(numbers1[i])
                stack2.append(numbers[i])
                fVal.append(-1)
                fval2.append(-1)
                break
            if(stack[-1] > numbers[i]):
                fVal.append(stack[-1])
                fval2.append(stack2[-1])
                stack.append(numbers1[i])
                stack2.append(numbers[i])
                break
            else:
                stack.pop()
fval2.reverse()
print(fval2)

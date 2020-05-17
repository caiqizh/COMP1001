import stack

def stockUp_saving(stock):
    up = len(stock)*[0]
    count = len(stock)*[0]
    aStack = stack.Stack()
    up[0] = 1  # the day starts from 0
    aStack.push(0)

    saving = 0
    for k in range(1,len(stock)):
        while not aStack.isEmpty() and stock[aStack.peek()] <= stock[k]:
            popped_day = aStack.pop()
            # calculate the saving for nonempty stack
            if not aStack.isEmpty():
                saving += 2 * (popped_day - aStack.peek() - 1)
            else:
                saving += 2 * popped_day
        # calculate the up period
        if aStack.isEmpty():
            up[k] = k+1
        else:
            up[k] = k - aStack.peek()
        aStack.push(k)
        #print(saving)
    saving = saving - (len(stock) - 1)
    
    return up,saving

stockPrice = [7, 12, 9, 6, 3, 9, 10, 11, 12]
#stockPrice = [7, 12, 9, 6, 3, 9, 10]
#stockPrice = [12,10,9,9,7,6,3]
#stockPrice = [3,6,7,9,9,10,12]
result,saving = stockUp_saving(stockPrice)
print("The total number of saving is", str(saving)+'.')

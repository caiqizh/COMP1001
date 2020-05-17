def reverseString(inStr):
    if inStr[-1] == '.':
        inStr = inStr[0:len(inStr)-1]
        outStr = inStr.split(' ')[::-1]
        outStr = ' '.join(outStr)+'.'
        return(outStr)
    else:
        outStr = list(inStr.split(' '))[::-1]
        outStr = ' '.join(outStr) 
        return(outStr)    

print("The correct output is:", reverseString("Here I am. Send me."))
print("The correct output is:", reverseString("Here I am. Send me!"))
print("The correct output is:", reverseString("All hard work brings a profit, but mere talk leads only to poverty."))
print("The correct output is:", reverseString("The beginning of wisdom is this: Get wisdom, and whatever you get, get insight."))


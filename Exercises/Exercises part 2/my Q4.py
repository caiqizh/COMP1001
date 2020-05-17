import stack
def isPalindrome(aString):
    aString = aString.lower()
    aStack = stack.Stack()
    
    if len(aString)%2 == 0:
        aStack.push(aString[0])
        for i in aString[1:]:
            if i != aStack.peek():
                aStack.push(i)
            if i == aStack.peek():
                aStack.pop()
        if aStack.size()==0:
            return 'True'
        else:
            return 'False'
    if len(aString)%2 == 1:
        a = list(aString)
        del a[int(len(aString)/2)]
        aStack.push(a[0])
        for i in a[1:]:
            if i != aStack.peek():
                aStack.push(i)
            if i == aStack.peek():
                aStack.pop()                
        if aStack.size()== 0:
            return 'True'
        else:
            return 'False'
print(isPalindrome('Rocky'))
print(isPalindrome('Hannah'))
print(isPalindrome('madam'))
print(isPalindrome('Hanna'))
print(isPalindrome('123321'))
print(isPalindrome('123456'))

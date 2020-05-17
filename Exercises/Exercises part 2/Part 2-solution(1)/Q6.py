import stack

def createPalindrome(str):
    strStack = stack.Stack()
    palindrome = ""
     
    for char in str:
        strStack.push(char)
         
    for char in str:
        palindrome += char
        palindrome += strStack.pop()

    return palindrome

def main():
    print(createPalindrome("abc"))
    print(createPalindrome("abcd"))
    print(createPalindrome("123456"))
    print(createPalindrome("654321"))
    print(createPalindrome("a"))
    print(createPalindrome(""))
    
main()

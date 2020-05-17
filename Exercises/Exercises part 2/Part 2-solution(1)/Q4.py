import stack

def isPalindrome(str):
    strStack = stack.Stack()
    palindrome = False
     
    for char in str:
        strStack.push(char.lower())
         
    for char in str:
        if char == strStack.pop():
            palindrome = True
        else:
            palindrome = False
             
    return palindrome

def main():
    print(isPalindrome("Rocky"))
    print(isPalindrome("Hannah"))
    print(isPalindrome("madam"))
    print(isPalindrome("Hanna"))
    print(isPalindrome("123321"))
    print(isPalindrome("123456"))

main()

def countChar():
    inputText = input("Please enter a word consisting of only English alphabets in lower cases: ")

    # create a list for counting the frequency of letters
    countChar = 26*[0]

    # count the letters in the word
    for letter in inputText:
        countChar[ord(letter)-97] += 1

    # print the frequency of letters in the word
    for index in range(0,26):
        print("# of "+chr(index+97)+" :", countChar[index])

countChar()
        
        
    

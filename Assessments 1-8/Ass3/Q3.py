import random

def guessNumber():
    lower, upper = eval(input("Please enter the lower and upper numbers, separated by a comma: "))
    print("The range of numbers is "+"["+str(lower)+"..."+str(upper)+"].")
    number = random.randint(lower,upper+1)
    attempt = 1
    while True:
        while True:
            guess = eval(input("Attempt #"+str(attempt)+": Please guess a number. "))
            if guess >= lower and guess <= upper:
                break
            else:
                print("Your input is out of range.")
                
        if guess > number:
            print("Your number is too big.")
            attempt += 1
        elif guess < number:
            print("Your number is too small.")
            attempt += 1
        else:
            print("Congratulation, you got it after",attempt,"guesses.")
            break

guessNumber()

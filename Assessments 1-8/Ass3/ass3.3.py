#Zhang Caiqi 18085481D
import random
k = 0
n = 1
a, b=eval(input('Please enter the lower and upper numbers, separated by a comma: '))
number = random.randint(a, b)
print('The range of number is ['+str(a)+'...'+str(b)+'].')
print('Attempt #'+str(n),end='') 
guess = eval(input(':Please guess a number. ') )

while True:
    if guess < a or guess > b:
        print('Your input is out of range.')
        print('Attempt #'+str(n),end='') 
        guess = eval(input(':Please guess a number. '))

    if guess < number and guess > a:
        n = n + 1
        print('Your number is too small.') 
        print('Attempt #'+str(n),end='') 
        guess = eval(input(':Please guess a number. '))   

    if guess > number and guess < b:
        n  = n + 1
        print('Your number is too big.')
        print('Attempt #'+str(n),end='') 
        guess = eval(input(':Please guess a number. ') )
            

    if guess == number:
        print('Congratulation, you got it after '+str(n)+' guesses.')   
        break
    


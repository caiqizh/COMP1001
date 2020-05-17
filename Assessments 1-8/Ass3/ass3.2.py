#Zhang Caiqi 18085481D
def squareRootTwo(n,a):
    x = a
    y = 1
    for i in range(n+1):
        if i == 0:
            print('n = ',i,'the number is: ',str(a)+'/'+'1')
            print('n = ',i,'using the radix point, the number is: ',float(a))
            print()
        else:
            u = x*x+2*y*y
            v = 2*x*y
            x = u
            y = v
            print('n = ',i,'the number is: ',str(x)+'/'+str(y))
            print('n = ',i,'using the radix point, the number is: ',u/v)
            print()

squareRootTwo(10,1)
squareRootTwo(10,10)
squareRootTwo(10,50)

# At first, we can find that the numbers using the radix point are totally different.
# But as the program going, the numbers become more and more approximate.
# At last, when n=10, the three numbers using radix point are exactly the same.
# The first reason is that when n is big enough, the number can gragually approach √2.
# The second reason is that python can only display 17 significant digits.
# And the three numbers are just the same in 17 significant digits.
          
    

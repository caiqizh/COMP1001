def squareRootTwo(n,a):
    # initially, a_0 = a/1
    numerator = a
    denominator = 1
    
    for i in range(n+1):
        print("n = ",i, "the number is: ",str(numerator)+'/'+str(denominator))
        print("n = ",i,"using the radix point, the number is: ",numerator/denominator)
        print()
        numerator_old = numerator
        # update the numerator and denominator by expressing a_n by num_n/den_n, where
        # num_n and den_n are the numerator and denominator of a_n, respectively.
        numerator = numerator_old**2 + 2*denominator**2
        denominator = 2*numerator_old*denominator

    return

squareRootTwo(10,1)
squareRootTwo(10,10)
squareRootTwo(10,50)

# Even with different initial conditions, their results will eventually converge.


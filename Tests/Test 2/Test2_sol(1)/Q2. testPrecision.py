num = 0.45
for i in range(1,9):
    for m in [1,2,25]:
        print("The value of {0} is {0:0.24f}".format(num), end="  ")
        print("m is {0:<4}:{1:0.25}".format(m,round(num,m)))
    num += 1
    print()

# For other cases, the fractional part is 0.5 which can be represented exactly as 0.1 in binary.
# However for 1.45, the truncated value is 1.4. Note that 0.4 cannot be represented exactly in binary.
    
print("The value of {0} is {0:0.40f}".format(0.45))
print("The value of {0} is {0:0.40f}".format(1.45))
print("The value of {0} is {0:0.40f}".format(2.45))
print("The value of {0} is {0:0.40f}".format(3.45))

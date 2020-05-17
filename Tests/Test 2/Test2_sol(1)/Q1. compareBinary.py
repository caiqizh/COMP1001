def compareBinary(s1, s2):
    """
    Input: s1 and s2 are strings of binary numbers which must
    contain the radix point.
    Output:
        Return 1 if the binary number in s1 is greater than that in s2.
        Return 0 if the binary number in s1 is equal to that in s2. 
        Return -1 if the binary number in s1 is less than that in s2.
    """

    s11 = (s1.lstrip('0')).rstrip('0')
    s22 = (s2.lstrip('0')).rstrip('0')

    if s11 > s22:
        return 1
    elif s11 < s22:
        return -1
    else:
        return 0


print(compareBinary("10.11","1.11"))
print(compareBinary("10.0","10.01"))
print(compareBinary("011.1","11.1"))
print(compareBinary("11.1","11.10"))
print(compareBinary("0.",".0"))

def bitLeftShift(binIn, n):
    """
    Input:
    - binIn: a binary number stored as a string. The most significant bit is stored as the first character in the string and so forth.
    - n: the number of bits to be shifted and n >= 0.
    Output: bin(binIn << n)
    """

    pos = 0
    allZero = True
    for digit in binIn:
        # break from loop if finding "1"
        if digit == "1":
            allZero = False
            break
        pos += 1

    # take care of the case of all 0
    if allZero == True:
        return "0"
    else:
        return binIn[pos:]+n*"0"


print("Test cases:")
print("Input: ", "00011, 3", "Output: ", bitLeftShift("00011", 3))
print("Input: ", "11111, 3", "Output: ", bitLeftShift("11111", 3))
print("Input: ", "00000, 3", "Output: ", bitLeftShift("00000", 3))
print("Input: ", "11111, 0", "Output: ", bitLeftShift("11111", 0))
print("Input: ", "10101, 5", "Output: ", bitLeftShift("10101", 5))
print("Input: ", "00001, 8", "Output: ", bitLeftShift("00001", 8))

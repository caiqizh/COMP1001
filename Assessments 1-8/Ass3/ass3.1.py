#Zhang Caiqi 18085481D
def bitLeftShift(binIn, n):
    binIn = binIn + '0'*n
    k = 0
    for i in binIn :
        if i == '0':
            k = k + 1 
        else:
            break
    binIn =binIn [k:]
    if binIn == '':
        return('0')
    else:
        return(binIn)



print("Test cases:")
print("Input: ", "00011, 3", "Output: ", bitLeftShift("00011", 3))
print("Input: ", "11111, 3", "Output: ", bitLeftShift("11111", 3))
print("Input: ", "00000, 3", "Output: ", bitLeftShift("00000", 3))
print("Input: ", "11111, 0", "Output: ", bitLeftShift("11111", 0))
print("Input: ", "10101, 5", "Output: ", bitLeftShift("10101", 5))
print("Input: ", "00001, 8", "Output: ", bitLeftShift("00001", 8))










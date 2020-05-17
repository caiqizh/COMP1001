
tableAdd = ["00", "01", "10"]

def PROC0(digit1, digit2):
    """
    Input: digit1, digit2, each of which is either 0 or 1.
    Output: a string of two digits which is the sum of the two digits. Therefore, the result could be "00", "01" or "10".
    """
    return tableAdd[digit1+digit2]

def PROC1(digit1, digit2, digit3):
    """
    Input: digit1, digit2, digit3, each of which is either 0 or 1.
    Output: a string of two digits which is the sum of the three digits. Therefore, the result could be "00", "01", "10", or "11".
    """
    firstPROC0Result = PROC0(digit1, digit2)
    secondPROC0Result = PROC0(int(firstPROC0Result[1]),digit3)
    if firstPROC0Result[0] == secondPROC0Result[0] == "0":
        result = "0"
    else:
        result = "1"

    return result+secondPROC0Result[1]


print(PROC1(0,0,0))
print(PROC1(0,1,0))
print(PROC1(1,0,0))
print(PROC1(0,0,1))
print(PROC1(0,1,1))
print(PROC1(1,0,1))
print(PROC1(1,1,0))
print(PROC1(1,1,1))


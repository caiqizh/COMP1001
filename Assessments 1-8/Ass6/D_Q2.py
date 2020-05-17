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

def PROC2(num1, num2):
    if len(str(num1)) > len(str(num2)):
        numBig = num1
        num2_Str = '0'*(len(str(num1))-len(str(num2))) + str(num2)
        num1_Str = str(num1)
    else:
        len(str(num1)) < len(str(num2))
        numBig = num2
        num1_Str = '0'*(len(str(num2))-len(str(num1))) + str(num1)
        num2_Str = str(num2)
    k = -1
    result = '00'
    list = []
    while k > -len(str(numBig)):
        a = result[0]
        result = PROC1(int(a),int(num1_Str[k]),int(num2_Str[k]))
        z = result[1]
        list.append(z)
        k = k-1

    Result = ''

    Result = PROC1(int(result[0]),int(num1_Str[k]),int(num2_Str[k]))
    list = list + [Result[1]] + [Result[0]]
    list = list[::-1]
    Ans = ''.join(list)
    return int(Ans)

print(PROC2(0,1))
print(PROC2(1,1))
print(PROC2(0,0))
print(PROC2(101,1))
print(PROC2(111,111))
print(PROC2(10101010,1111100))  



#Zhang Caiqi 18085481D
def PROC1(digit1,digit2,digit3):
    def PROC0(digit1,digit2):
        tableAdd = ['00', '01', '10']
        #These are the only possible outcomes of adding two binary digits
        if digit1 + digit2 == 0:
            return(tableAdd[0])
        if digit1 + digit2 == 1:
            return(tableAdd[1])
        if digit1 + digit2 == 2:
            return(tableAdd[2])

    digit12 = PROC0(digit1,digit2)
    digit123 = PROC0(int(digit12[1]),digit3)
    if digit12[0] == '0' and digit123[0] == '0':
        return('0'+digit123[1])
    else:
        return('1'+digit123[1])
print(PROC1(0,0,0))
print(PROC1(0,1,0))
print(PROC1(1,0,0))
print(PROC1(0,0,1))
print(PROC1(0,1,1))
print(PROC1(1,0,1))
print(PROC1(1,1,0))
print(PROC1(1,1,1))

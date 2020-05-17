def compareStrings(s1, s2):
    if len(s1) > len(s2):
        s1c = s1[:len(s2)]
        s2c = s2
    else:
        s1c = s1
        s2c = s2[:len(s1)]
        k = ''
    for i in range(len(s1c)):
        if s1c[i] > s2c[i]:
            return '>'
            
        if s1c[i] < s2c[i]:
           return '<'
            
        if s1c[i] == s2c[i]:
            pass
    if len(s1) > len(s2):
        return ">"
    elif len(s1) < len(s2):
        return "<"
    else:
        return "="

                    

    return k


print(compareStrings("alpha","omega"))
print(compareStrings("omega","alpha"))
print(compareStrings("alphaomega","alphaomega"))
print(compareStrings("","omega"))
print(compareStrings("Benjamen","Ben"))
print(compareStrings("",""))

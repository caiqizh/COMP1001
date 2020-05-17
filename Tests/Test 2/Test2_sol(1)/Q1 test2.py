def compareBinary(s1,s2):
    s1=s1.lstrip('0')
    s1=s1.rstrip('0')
    s2=s2.lstrip('0')
    s2=s2.rstrip('0')
    a = 0
    b = 0
    for j in s1:
        if j == '.':
            break
        else:
            a += 1
    for j in s2:
        if j == '.':
            break
        else:
            b += 1
  
    if a > b:
        return ('1')
    if a < b:
        return ('-1')
    if a == b:
        s1d = s1[a+1:]
        s2d = s2[b+1:]
        s1d.lstrip('0')
        s1d.rstrip('0')
        s2d.lstrip('0')
        s2d.rstrip('0')
        a = 0
        b = 0
        for j in s1[a+1:]:
            a += 1
        for j in s2[b+1:]:
            b += 1
        if a > b:
            return 1
        if a < b:
            return -1
        else:
            return 0
print(compareBinary("10.11","1.11"))

print(compareBinary("10.0","10.01"))
print(compareBinary("011.1","11.1"))

print(compareBinary("11.1","11.10"))

print(compareBinary("0.",".0"))

    
        
